# Write Up One Line LFI Challenge JHack Semi Final CTF

Pada challenge kali ini dengan point paling tinggi dikategorynya dan tidak diberikan sourcenya, Dan menurut saya pribadi challenge ini yang paling `tricky`

Kite pertama diberikan sebuah page login

![](/JHackCTF/Picture/img/login.png)


Seperti biasa jika diberikan sebuah login page saya akan mencoba teknik2 yang umum. Setelah beberapa saat cukup kesulitan untuk masuk dengan berbagai payload sqli ternyata login ini masuk dengan param tampering di bagian username dengan kita memasukan sebuah array pada namenya `[]`

![](/JHackCTF/Picture/img/array.png)

Setelah masuk kita diberikan form seperti ini tampilanya.

![](/JHackCTF/Picture/img/home.png)

Pada form tersebut kita diberikan sebuah link sample untuk dimasukan ke form tersebut.

`https://www.wowkeren.com/display/images/photo/2018/11/16/00232349.jpg`

Dan output yang diperoleh adalah seperti ini.

![](/JHackCTF/Picture/img/dh.png)

Oke saat kita mencoba memasukan link lain.

![](/JHackCTF/Picture/img/err.png)


Oke mendapatkan sebuah alert error tersebut. Jadi kita hanya boleh memasukan web `https` dan file berakhiran `.jpg` 

Karena saya kebetulan mempunyai website ber SSL pertama saya membuat file `.jpg` kosong dan memasukan nya. Dan melihat responsenya di brupsuite!

![](/JHackCTF/Picture/img/r1.png)

Seperti itulah responsenya. Oke oke mari kita coba isi gambar tersebut dengan kode kode php.

Inilah kode php yang saya isikan `<?php echo 1; ?>`

![](/JHackCTF/Picture/img/r1.png)


Hmmm mendapatkan response seperti itu. Jadi kode kita tetap tidak tereksekusi. Asumsi saya tidak tereksekusi karena format yang saya di server masih `.jpg` saya harus merubah `.jpg` menjadi `.php` muncul ide saya di server saya mengunakan `.htaccess` untuk `rewrite` file saya yang `.jpg` ke `shell.php` Dengan cara.

```
RewriteEngine On
RewriteRule ^image.jpg$ shell.php
```

Sekarang isi dari `shell.php` adalah `<?php echo exec('whoami'); ?>` 

Dan saat dimasukan!

![](/JHackCTF/Picture/img/s1.png)


Yeahh!! keluar `www-data` Namun itu adalah `whoami` dari server saya! Hmm kita tinggal merubah payloadnya agar dapat melakukan local read file. Saya mengunakan payload ini

```
header("LOCATION: php://filter/convert.base64-encode/resource=index.php");
```

Dan didapatkan responseee seperti ini..

![](/JHackCTF/Picture/img/s2.png)

Woaaaa Successs!!! 

![](/JHackCTF/Picture/img/flag.png)

Didapatkanlah flagnya saat mengakses file tersebut!

Sekian Write Up Kali ini Terima Kasih!


