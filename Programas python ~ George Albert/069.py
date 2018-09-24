print('\033[1;32m~'*30)
print('BANCO DE DADOS ')
print('~'*30)
amigos = 0
man = 0
totalman = 0
mulher = 0
while True:
    Amigos = str(input('\nAmigos: '))
    amigos += 1

    idade = int(input('\nIdade: '))

    sexo = ' '

    continuar = ' '

    while sexo not in 'MF':
        sexo = str(input('\nSexo: [M/F] ')).strip().upper()[0]

    while continuar not in 'SN':
        continuar = str(input('\nContinuar? [S/N]')).upper().strip()[0]

    if idade >= 18 and sexo == 'M':
        man += 1

    if sexo == 'M':
        totalman += 1

    if sexo == 'F':
        mulher += 1

    if continuar == 'N':
        break
print('~'*50)
print(f'''\nAmigos maiores de 18 {man}
        \nAmigos homens {totalman}
        \nTotal de Amigos {amigos}
        \nAmigas mulheres {mulher}''')
print('~'*50)

