from time import sleep
import emoji
print('\033[1;31m='*100)
print(f'{"LISTAS!":^100}')
print('='*100)
print('''\033[1;31m                                          root@hastein
                         ``               OS: Kali Linux 
                        `-.               Kernel: x86_64 Linux 4.17.0-kali1-amd64
       `               .---               Uptime: 18h 41m
     -/               -::--`              Packages: 2978
   `++    `----...```-:::::.              Shell: bash
  `os.      .::::::::::::::-```     `  `  Resolution: 1920x1080
  +s+         .::::::::::::::::---...--`  DE: GNOME 
 -ss:          `-::::::::::::::::-.``.``  WM: GNOME Shell
 /ss-           .::::::::::::-.``   `     WM Theme: Kali-X
 +ss:          .::::::::::::-             GTK Theme: Adwaita-dark [GTK2/3]
 /sso         .::::::-::::::-             Icon Theme: gnome
 .sss/       -:::-.`   .:::::             Font: Cantarell 11
  /sss+.    ..`  `--`    .:::             CPU: Intel Core i3-6006U @ 4x 2GHz [44.0°C]
   -ossso+/:://+/-`        .:`            GPU: Mesa DRI Intel(R) HD Graphics 520 (Skylake GT2) 
     -/+ooo+/-.              `            RAM: 3132MiB / 3858MiB                               
''')
print('='*100)
print(f'{"LISTAS!":^100}')
print('='*100)
valor = list()
while True:
    n = (int(input('\n\033[1;30mDigite um número: ')))
    sleep(1)
    if n in valor:
        print('\n\033[1;31mValores iguais não posso adcionar!\033[m\033[1;34m')
        sleep(1)
    else:
        print('\n\033[1;34mAdcionado com sucesso!\033[m')
        valor.append(n)
    continuar = ' '
    continuar = str(input("\n\033[1;30mQuer continuar? [S/N]: ")).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('\n\033[1;31mVocê digitou errado! Quer continuar? [S/N]: ')).upper().strip()[0]
        sleep(1)
    if continuar == 'N':
        break
n = max(valor)
valor.sort()
print('\nOs valores digitados foram: ', end='')
for b in valor:
    print(f'\033[1;34m[{b}]\033[m ', end='')
    sleep(1)
    print('\033[1;34m⇜⇝ 'if b < n else '\033[1;30m= FIM ', end='')
