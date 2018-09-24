print('\033[1;30m')
valores = [[0,0,0], [0,0,0], [0,0,0]]
par = cont = maior = 0
for l in range(0,3):
    for a in range(0,3):
        valores[l][a] = int(input(f'Digite o valor para [{l},{a}]: '))
print('\n'*50)
for l in range(0,3):
    for a in range(0, 3):
        print(f'[{valores[l][a]:^5}]', end='')
        if valores[l][a] % 2 == 0:
            par += valores[l][a]
    print()
for l in range(0,3):
    cont += valores[l][2]
for a in range(0,3):
    if a == 0:
        maior = valores[1][a]
    elif valores[1][a] > maior:
        maior = valores[1][a]
print('\n'*2)
print(f'Soma dos valores pares: [{par}]')
print()
print(f'Soma dos valores da 3º coluna: [{cont}]')
print()
print(f'Maior valor da 2ª coluna: [{maior:^5}]')
