from random import randint
from time import sleep

comp = (randint(1,20),
        randint(1,20),
        randint(1,20),
        randint(1,20),
        randint(1,20),
        randint(1,20),
        randint(1,30),
        randint(35,45))
print('''\033[1;36m                  ._`        
                  .o+`                 root@hastein
                 `ooo/                 OS: Kali Linux 
                `+oooo:                Kernel: x86_64 Linux 4.17.0-kali1-amd64
               `+oooooo:               Uptime: 6h 45m
               -+oooooo+:              Packages: 2978
             `/:-:++oooo+:             Shell: bash
            `/++++/+++++++:            Resolution: 1920x1080
           `/++++++++++++++:           DE: GNOME 
          `/+++ooooooooooooo/`         WM: GNOME Shell
         ./ooosssso++osssssso+`        WM Theme: Kali-X
        .oossssso-````/ossssss+`       GTK Theme: Adwaita-dark [GTK2/3]
       -osssssso.      :ssssssso.      Icon Theme: gnome
      :osssssss/        osssso+++.     Font: Cantarell 11
     /ossssssss/        +ssssooo/-     CPU: Intel Core i3-6006U @ 4x 2GHz [47.0°C]
   `/ossssso+/:-        -:/+osssso+-   GPU: Mesa DRI Intel(R) HD Graphics 520 (Skylake GT2) 
  `+sso+:-`                 `.-/+oso:  RAM: 2869MiB / 3858MiB
 `++:.                           `-/+/
 .`                                 `/''')
print('='*100)
print('{:^100}'.format('Sorteando!!!'))
print('='*100)

while True:
    pergunta = ' '
    pergunta = str(input('Iniciar o progrma? [S/N]: ')).upper().strip()[0]
    while pergunta not in 'SN':
        print('Você Digitou errado digite novamente! ', end='')
        pergunta = str(input('Iniciar o progrma? [S/N]: ')).upper().strip()[0]
    if pergunta == 'S':
        print('='*100)
        print('{:^100}'.format('[INICIANDO O PROGRAMA, BEM VINDO]'))
        print('='*100)
        sleep(2)
        print('Os números sorteados foram: ', end='')
        for c in comp:
            if c <= 6:
                print(f'\033[1;32m[{c}] ⇜⇝ \033[m', end='')
                sleep(1)
            else:
                if c == 20:
                    print(f'\033[1;31m[{c}] ⇜⇝ \033[m', end='')
                    sleep(1)
                if c >= 20:
                    print(f'\033[1;34m[{c}] ⇜⇝ \033[m', end='')
                    sleep(1)
                if c >= 35:
                    print(f'\033[1;35m[{c}]\033[m', end='')
                    print('\033[1;35m = FIM 'if c > 35 else '', end='')
                    sleep(1)
                else:
                    print(f'\033[1;33m[{c}] ⇜⇝ \033[m', end='')
                    sleep(1)
        print(f'\n\n\033[1;36mO maior número gerado foi: [0{max(comp)}] ')
        sleep(1)
        print(f'\nO menor número gerado foi: [0{min(comp)}] ')
        sleep(1)
        break
    else:
        if pergunta == 'N':
            print('\nSaindo.................................................................')
            sleep(5)
            print('\nPrograma encerrado volte sempre!!!')
            sleep(5)
            break

