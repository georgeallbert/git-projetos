print('''\033[1;32m   
    ..:.:.               
   ..:.:.:.:.            
  ..:.:.:.:.:.:.          
 ..:.:.:.:.:.:.:.:.       
   .:.::;.::::..:.:.:.   
      .:.:.::.::.::.;;/   
         .:.::.::://///   root@hastein
            ..;;///////   OS: Kali Linux 
            ///////////   Kernel: x86_64 Linux 4.17.0-kali1-amd64
         //////////////   Uptime: 8h 38m
      /////////////////   Packages: 2978
   ///////////////////    Shell: bash
 //////////////////       Resolution: 1920x1080
  //////////////          DE: GNOME 
   //////////             WM: GNOME Shell
    //////                WM Theme: Kali-X
     //                   GTK Theme: Adwaita-dark [GTK2/3]
    ..:.:.                Icon Theme: gnome
   ..:.:.:.:.             Font: Cantarell 11
  ..:.:.:.:.:.:.          CPU: Intel Core i3-6006U @ 4x 2GHz [45.0°C]
 ..:.:.:.:.:.:.:.:.       GPU: Mesa DRI Intel(R) HD Graphics 520 (Skylake GT2)
   .:.::;.::::..:.:.:.    RAM: 2633MiB / 3858MiB
      .:.:.::.::.::.;;/   
         .:.::.::://///   
            ..;;///////    
            ///////////   
         //////////////   
      /////////////////   
   ///////////////////   
 //////////////////       
  //////////////          
   //////////              
    //////                
     //''')
perg = (int(input('\033[1;32m\nDigite o primeiro número: ')),
        int(input('\nDigite o segundo número: ')),
        int(input('\nDigite o terceiro número: ')),
        int(input('\nDigite o último número: ')))

if 9 in perg:
     print(f'\nO valor \033[1;31m[9]\033[m\033[1;32m foi digitado {perg.count(9)} vezes ')
else:
     print('\nO valor  \033[1;31m[9]\033[m\033[1;32m não foi digitado')
if 3 in perg:
     print(f'\nO valor \033[1;35m[3]\033[m\033[1;32m foi digitado na posição {perg.index(3)} ')
else:
     print('\nO valor \033[1;30m[3]\033[m\033[1;32m não foi digitado! ')
print('Os números pares são: ', end='')
for c in perg:
    if c % 2 == 0:
        print(f'\033[1;35m[{c}] ', end='')

