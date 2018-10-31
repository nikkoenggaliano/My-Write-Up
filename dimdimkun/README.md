# Write UP Challenge 

Pertama untuk soal ini saya tidak akan membahas tentang Reverse Engineering. Tapi akan membedah tentang source codenya.

Pertama kita buka `antiweeb.c` dan kita compile dengan ketentuan yang sudah saya catat pada source tersebut!

Mari kita bedah sourcenya.


```if(strlen(input) == 19){``` Pada bagian ini input kita harus panjangnya 19 Karakter 

```if((int)input[4]==45 && (int)input[9]==45 && (int)input[14] == 45)``` Pada bagian tersebut input kita pada index ke `4/9/15` Harus bernilai interger `45`


Dengan kata lain kita bisa berandai-andai bahwa input kita berbentuk seperti ini
1234-1234-1234-1234

Tapi ada validasi terakhir seperti ini.

```if(check == (i / ((20*4)+(3+2)*(2*2))) - d)``` 

Variable check ini harus sama dengan operasi matematika `(i / ((20*4)+(3+2)*(2*2))) - d` Mari kita bedah satu persatu variable pembandingnya!

variable check dibuat dari ini

```for(int i=0; i<strlen(input); i++){ check += (int)input[i]; }```

Yang maksudnya adalah setiap inputan kita diconver ke decimal dan ditambahkan.


Lalu operasi matematika didapatkan dari ini.

```
int p = (strlen(input)*strlen(input)) - strlen(input);
int d = p * 2;
int i = d * p;
int check = 0;
```

p bernilai (19*19-19) = 342
d bernilai (342*2) = 684
i bernilai (684*342) = 233928

Jadi operasi ini `(233928 / ((20*4)+(3+2)*(2*2))) - 684` Menghasilkan angka `1655` 

Maka dari itu inputan kita harus berbentuk seperti ini

0000-0000-0000-0000 tapi jika ditotal hasil convert decimalnya semua harus bernilai 1655 maka saya membuat solver automatis untuk mencari nilai tersebut! 

Silahkkan dijalankan dan mendapatkan flag!
