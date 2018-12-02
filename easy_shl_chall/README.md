Oke kali ini akan membahas <b>Surabaya Hacker Link</b> Challenge. Tapi ini bukan Challenge untuk masuk ke groupnya ya, Tapi ini challenge yang kebetulan ada!

Dikala saya membuka `Telegram` Saya membaca group dan ada `Admin` memberikan info sebagai berikut.

![](/easy_shl_chall/admin.png)

Kita diberikan challenge dengan info sebagai berikut.

Target : http://110.93.14.30/

Dan saat target dibuka 

![](/easy_shl_chall/index.png)

Ada tampilan `Apache Default Debian` Nah dan setelah saya telusuri, Tidak ada yang begitu menarik sih. Langkah selanjutnya kita lakukan `Reconnaissance` Pada target tersebut.

Saya scan dengan `Nmap` Dahulu.

`$ nmap -T4 -A -v 110.93.14.30`

`-T4` Ini berati set Performance

`-A` Mendeteksi OS , version , script scanning, dan traceroute

`-v` Untuk Verbose

Dan saya mendapatkan Output Seperti ini.

```
22/tcp   open     ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 e2:3e:29:1d:86:70:57:ea:1b:d6:68:84:e9:30:df:17 (RSA)
|   256 77:d2:22:dd:0a:ae:8e:86:28:94:30:8a:ad:ba:b1:2a (ECDSA)
|_  256 d5:29:71:e6:37:95:b2:7c:d3:fb:4b:17:7c:30:45:fa (ED25519)
25/tcp   filtered smtp
80/tcp   open     http        Apache httpd 2.4.18 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Easy Challenge SHL
139/tcp  open     netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open     netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
9090/tcp filtered zeus-admin
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3.13 cpe:/o:linux:linux_kernel:4.2
OS details: Linux 3.13 or 4.2
Service Info: Host: UBUNTU; OS: Linux; CPE: cpe:/o:linux:linux_kernel


Host script results:
|_clock-skew: mean: -2h19m59s, deviation: 4h02m28s, median: 0s
| nbstat: NetBIOS name: UBUNTU, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   UBUNTU<00>           Flags: <unique><active>
|   UBUNTU<03>           Flags: <unique><active>
|   UBUNTU<20>           Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|_  WORKGROUP<1e>        Flags: <group><active>
| smb-os-discovery:
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: ubuntu
|   NetBIOS computer name: UBUNTU\x00
|   Domain name: \x00
|   FQDN: ubuntu
|_  System time: 2018-12-02T14:47:37+07:00
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2018-12-02 14:47:37
|_  start_date: N/A
```

Oke hal yang paling menarik adalah. Ada sebuah smbclient yang terbuka, Mari kita coba buka koneksi smbnya. Melihat hal hal yang mungkin ada.

```
$smbclient -L 110.93.14.30
WARNING: The "syslog" option is deprecated
Enter root's password:
Domain=[WORKGROUP] OS=[Windows 6.1] Server=[Samba 4.3.11-Ubuntu]

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        solver          Disk
        IPC$            IPC       IPC Service (ubuntu server (Samba, Ubuntu))
Domain=[WORKGROUP] OS=[Windows 6.1] Server=[Samba 4.3.11-Ubuntu]

        Server               Comment
        ---------            -------
        UBUNTU               ubuntu server (Samba, Ubuntu)

        Workgroup            Master
        ---------            -------
        WORKGROUP            UBUNTU
```

Terlihat disitu ada sebuah sharename solver persis seperti clue pada webnya. Tinggal kita connect

```
$smbclient //ubuntu/solver -I 110.93.14.30 -N
                
WARNING: The "syslog" option is deprecated
Try "help" to get a list of possible commands.
smb: \> help
?              allinfo        altname        archive        backup         
blocksize      cancel         case_sensitive cd             chmod          
chown          close          del            deltree        dir            
du             echo           exit           get            getfacl        
geteas         hardlink       help           history        iosize         
lcd            link           lock           lowercase      ls             
l              mask           md             mget           mkdir          
more           mput           newer          notify         open           
posix          posix_encrypt  posix_open     posix_mkdir    posix_rmdir    
posix_unlink   posix_whoami   print          prompt         put            
pwd            q              queue          quit           readlink       
rd             recurse        reget          rename         reput          
rm             rmdir          showacls       setea          setmode        
scopy          stat           symlink        tar            tarmode        
timeout        translate      unlock         volume         vuid           
wdel           logon          listconnect    showconnect    tcon           
tdis           tid            logoff         ..             !    

```

Nah disitu kita sudah Mendapatkan akses smb ke share `solver` kita tinggal put aja file name Kita agar terterah di Solver :D

Sekian Terima Kasih.

Nikko Enggaliano

