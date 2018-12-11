# Write Up Blind RCE JHack Semi Final CTF

Pertama kita diberikan sebuah web tapi webnya sudah mati, jadi saya coba di local saja, Namun kita diberikan source codenya

![](/JHackCTF/Blind/img/index.png)

Seperti itulah penampakan source codenya.


Mari kita petakan source itu ngapain aja.

```
<?php
$sandbox = dirname(__FILE__) . '/'  .md5($_SERVER['REMOTE_ADDR']);
@mkdir($sandbox);
copy(dirname(__FILE__) . '/' . ".htflag",  $sandbox . "/.htflagsandboxzazsdmno");
@chmod($sandbox);
@chdir($sandbox);

```

Pada kode tersebut variable $sandbox berisi parent dir dari tempat soal tersebut dan ditambah remote address kita. Lalu `@mkdir` Dibuatlah dir menurut remote address kita, lalu `copy` melakukan duplikasi flag utama ke dir kita dengan nama `.htflagsandboxzazsdmno`

```
if (isset($_GET['reset'])) die(exec('/bin/rm -rf ' . $sandbox));
```

Pada kode tersebut, jika ada parameter get `reset` maka dir kita akan di hapus.

```
$command = substr(urldecode(trim(file_get_contents('php://input'))), 1, 10);
if (strpos($command, '*') !== false) die("* di blacklist om");
@exec($command);
```

Pada kode tersebut variable $command berisi 10 input POST data kita. Dan di check apakah inputan kita mengandung `*` jika tidak maka akan dilakukan command shell. But tidak ada output jadi kita tidak tau apakah command inputan kita berhasil menjalankan atau tidak!

Oke ide pertama saya adalah melakukan direct acces ke flag `.htflagsandboxzazsdmno` dengan dir remote address kita namun gagal :(( 

![](/JHackCTF/Blind/img/fail.png)

403 Forbidden saat saya mencoba direct akses flag tersebut. Ngomong ngomong jika pingin mengetahui remote address kita bisa mengunakan bantuan `whoer.net` disitu tinggal md5 saja ip kalian.

Jadi idenya adalah kita melakukan `cat .htflagsandboxzazsdmno` dan mengarahkan nya ke file baru, Karena saat saya cek melakukan post data `echo "" > a` ternyata file `a` memang ada dan dapat diakses.

Oke ide selanjutkan kita merancang payload untuk melakukan `ls -atr` dan `cat .htflagsandboxzazsdmno` dan payload saya berbentuk seperti pada `exploit.php`

Saat dijalankan!

![](/JHackCTF/Blind/img/flag.png)


Sudah dapatlah flagnya `JHack2018{Next_Level_Exec}` 

