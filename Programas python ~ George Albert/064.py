cont = 0
soma = 0
while True != 999:
    n = int(input('\033[1;34mDoigite um valor: '))
    cont += 1
    soma += n
    if n == 999:
        print('~'*50)
        print(f'Você digitou {cont - 1} números  A soma de todos é igual a {soma - 999}')
        print('~'*50)
        break
