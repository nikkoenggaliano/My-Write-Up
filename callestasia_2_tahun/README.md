# Setelah 2 tahun perginya Callestasia, apa saja yang berubah?



Assalamualaikum Warahmatullahi Wabarakatuh. Pagi ini hari Minggu, saya seperti biasa streaming Anime favorit saya lalu sembari bermain media sosial. Setelah menanggapi salah satu cuitan di Timeline soal Cyber Security dan Defacing, saya jadi ingat pernah menangani kasus defacing dan kasus yang bukan deface, tapi bisa mengarah ke sana. 



Kasus yang saya alami adalah pada platform Belajar Cyber Security yang dihack. "Platform hacker kok dihack" Yayaya, saya sudah sering dapat kata-kata itu, tapi kesalahan menuju kesuksesan kan? Kejadiannya sudah 2 tahun lalu lebih, tepatnya Hari H ulang tahun saya, dan saya patching H+1. Saya pernah menuliskan hal itu di blog Callestasia, karena domainnya mati dan tidak bisa dibackup DBnya, berikut ini web archivenya.



https://web.archive.org/web/20180712062535/http://blog.callestasia.org/2018/05/09/sayonara-ctf-callestasia/



Saya akan mengcopy semua tentang Proses Callestasia di tautan di atas, lalu memperbaiki di bawah ini.





# Sayonara CTF Callestasia 



Oke kita ke pokok masalah. Sebenernya saya mengembangkan sebuah platform CTF yang ber subdomain di https://ctf.callestasia.org. Platform itu  sebenernya punya nya mas Eka Syahwan. Saya kembangkan lagi, kemarin  Tepat malam ulang tahun saya. Di group chat telegram SHL, ada salah satu anggota  yang mengeluh ada user yang mencapai nilai yang tidak masuk akal 21xxxx dan 999999. Seperti yang dapat dilihat pada gambar di bawah ini.



![](.\src\img\photo-2018-05-09-17-18-33.jpg) 



Karena di situ sudah jam tidur saya dan saya kebetulan sedang jadi Bucin baru pada saat itu, Saya tidak begitu fokus melihat ke platform saya ini.  Saya cuman login admin dan men-delete akun tersebut. Tapi paginya User tersebut muncul lagi wkwk. Apa yang saya lakukan? Analisa dimulai.



**Step Pertama saya**:



Mulai mengecek `/var/log/apache2/access.log` . Setelah saya baca dengan **saksama.** Ada sebuah access dari user menggunakan user agent `curl`. Seperti inilah hasil setelah saya lakukan `grep` pada `access.log` dengan filter `curl`



![](.\src\img\curl.png)



Ada seseorang melakukan GET & POST request ke `/admin/tambahuser` yang mana end-point tersebut digunakan untuk meng-inputkan user baru. Lalu saya cepat cepat melihat `source code` pada url tersebut, seperti inilah isinya.



![](.\src\img\ear.png)

Nah seperti di atas lah sourcenya.  Sudah sangat jelas ternyata ada sebuah bug**[ Execution After Redirect (EAR)](https://web.archive.org/web/20180712062535/https://www.owasp.org/index.php/Execution_After_Redirect_(EAR))** yang mana attacker dapat menjalankan sisa script setelah `redirect` dilakukan. Yang mana konsep `header("location")` hanya memberikan HTTP response yang mana akan dirender oleh browser atau sisi client, namun sebenarnya sisa dari scriptnya masih berjalan, dengan menggunakan tools `curl` kita dapat mengabaikan HTTP responsnya lalu dapat melihat form dan melakukan submit post tanpa auth. Jadi, bagaimana kita dapat melakukan patchingya? Sederhana, kita cukup mematikan script setelah redirect dijalankan seperti ini.



```php
if(isset($_SESSION['username']) == ""){
    header("Location: login.php");
    exit;
}
```



Sangat sederhana bukan, dengan menambahkan `exit;` pada code yang melakukan HTTP redirect, kita akan aman dari serangan `EAR` dengan implementasi yang benar tentunya.



Lalu di situ si hacker melakukan POST data ke end-point `/admin/tambahuser`.  Terdapat kesalahan yang sama, jika fungsi redirect di atas bermasalah, maka semuanya juga akan bermasalah. Di mana POST data dari form yang seharusnya mempunyai auth akan dapat dijalankan tanpa sesi, dan yang pasti karena kodenya juga satu file, tapi seperti inilah isi dari source code yang juga mempunyai BUG yang hampir mirip karena tidak benarnya menangani redirect.



![](.\src\img\csrf.png)



Pada kode di atas terdapat bug yang sebenarnya tidak akan terjadi jika penanganan redirect user yang belum mempunyai sesi yang tepat di-redirect dengan baik. Tapi tak apa, nama BUGnya yaitu CSRF. Intinya karena tidak punya sesi dan tidak adanya token unique pada form yang dirender, attacker dengan bebas untuk melakukan POST data, tinggal mengikuti `name` pada form yang sudah ter-render dengan `curl` saja. Kurang lebih seperti ini payloadnya.



```sh
curl -X POST –data "name=thanos&Password=asdasd&universita=ajaja&status=1&point=999999" (url)
```



Lalu bagaimana kita dapat mencegah serangan `csrf` ini jika memang kita terkena bug `EAR`  tapi yang jadi masalah utama di sini adalah `EAR` kita harus menyelesaikan BUG `EAR` agar dapat juga mencegah `csrf` tapi baiklah. Salah satu cara untuk menangani `csrf` ini adalah dengan menambahkan `unique` token dari SESSION yang digenerate secara random, seperti inilah contoh script sederhananya,



```php
if (!isset($_SESSION[‘nay’])) { $_SESSION[‘nay’] = md5(‘nepska’.time().time().’nayeon’); }
    if(isset($_SESSION['nay']) != “”){
   		unset($_SESSION['nay']);
    	header(“Location: index.php”);
		exit;
    }
```

Itu mengenerate session tokenya. Dan di-form saya tambahkan hidden value seperi di bawah ini.



```htm
<input type=”hidden” name=”nayeon” value=”<?= $SESSION[‘nay’] ?>”>
```



Lalu proses pengecekannya saat ada submit form data menjadi seperti ini.



```PHP
if(isset($_POST['name'],$_POST['Password'],$_POST['univeristas'],$_POST['status'],$_POST['point'],$_POST['nayeon'])){
	
    if($_POST['nayeon'] != $SESSION['nay'])
    {
    	die('INVALID TOKEN');
    }

    $status = $Database->tambahkan_user($_POST['name'],md5($_POST['Password']),$_POST['univeristas'],$_POST['status'],$_POST['point']);
    if($status){
    	header("Location: manage-member");
    }
}
```



Seperti itulah proses `patching` yang saya lakuka. Tapi itu dilakukan 2018, kalau sekarang, pasti saya lebih memilih menggunakan `framework` agar proses manual securityna dapat dilewati, karena secara default `framework` akan lebih aman soal proses manual redirect ataupun token-csrfnya.



Dan dengan ini saya juga menutup service CTF Callestasia saya. Bukan  karena kasus terhack ini tapi dengan saya ingin membuat dari 0 platform ini untuk lebih nyaman digunakan 😀

Note to Hackernya. Terima Kasih banyak. Berkat adanya dirimu saya lebih banyak belajar lagi. Dan jika berkenan saya sekali lagi ucapkan Terima Kasih 😀 Saya tidak ada dendam apapun kok, Jika bug itu di-exploitasi oleh hacker jahat mungkin akan dilakukan hal hal yang lebih menakutkan misalnya delete akun user, Tapi hacker ini hanya iseng  menambah akun dengan point besar aja.

Terima Kasih Untuk semua Player CTF Callestasia kami akan kembali secepat mungkin 😀



### Setelah kejadian itu



Setelah kejadian di atas, lalu setelah menuliskan artikel dan saya share, actor dari attacking tersebut menghubungi saya lewat `Facebook` untuk meminta maaf, semua berjalan dengan sopan baik dan nyaman.  BTW saat proses mencari chat sang actor, saya baru sadar sudah bertemu sama actornya secara langsung berkali-kali dan sudah berteman baik juga sampai sekarang haha benar-benar komedi dunia ini.





# Lalu apa yang terjadi setelah 2 tahun ini?



Setelah 2 tahun setelah kejadian di atas, dan tepatnya pada 2020 ini pada musim pandemi COVID-19 ini, saya merasakan perubahan yang sangat banyak bertemu teman-teman yang sefrekuensi dengan saya. Dari alumni TK Cemara, teman-teman Solo yang bukan asli Solo. dan banyak lainya, semuanya berkat Callestasia ini. Hal yang paling signifikan berubah selain saya adalah teman-teman saya, contoh paling nyata adalah nickname `kosong` yang di scoreboard di atas rankingnya masih 'cupu' namun sekarang? Dia sendiri bagi saya dan teman-teman satu circle setara dengan 3 orang, Ini serius tidak berlebihan.



Lalu setelah kejadian hacking di atas, apakah Callestasia sempat hidup lagi? Iya. Tapi tidak lama, karena keterbatasan resource dan waktu untuk maintainancenya, namun sempat 1 kali Platform `Callestasia New` Berjalan untuk kompetisi resmi besar, yaitu *CTF SHL 2018* yang di selengarakan di universitas Narotama Surabaya, Di mana nickname `Kosong` menjuarai (1) dan `Tukang Sihir` juara (2). Kedua orang ini bagi kami 1 circle adalah anak muda yang sangat berbakat, Kita ber 3 di tahun 2020 ini mengikuti CTF Internasional dan menempati urutan ke 10 dari 200 an peserta. Ya, bagi saya Callestasia ini adalah jalan rejeki saya, rejeki bertemu teman-teman yang sangat baik, banyak sekali. 



Lalu, setelah ini ada apa? Saya akan menghidupkan ulang Callestasia, dengan brand yang sama namun domain yang berbeda(?) Tapi tidak hanya Hacking Platform, juga ada tempat untuk belajarnya (Course Section) pertulisan ini diketik, sudah lebih dari 50% aplikasinya jadi, Kenapa buat lagi-lagi dan lagi? Karena saya juga butuh ngoding buat memperkaya logika saya.





# Terima Kasih untuk semua yang bagian dari Callestasia.

Terima kasih Callestasia, Terima kasih teman-teman di belakang layar yang tidak dapat saya sebutkan satu persatu, dengan adanya platform ini, kita dapat bertemu secara nyata, kita sampai detik ini berkembang bersama. Terima kasih, mari lanjutkan perkembangan diri kita ini bersama-sama.