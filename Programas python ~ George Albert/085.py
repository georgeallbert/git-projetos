print('\033[1;30m')
dimen = [[], [], []]
matriz = True
soma = 1
par = 1
maior = menor = 0
for a in range(0,3):
    matriz = int(input(f'Digite um valor para: [0, {a}] '))
    dimen[0].append(matriz)
for b in range(0,3):
    matriz = int(input(f'Digite um valor para: [1, {b}] '))
    dimen[1].append(matriz)
for c in range(0,3):
    matriz = int(input(f'Digite um valor para: [2, {c}] '))
    dimen[2].append(matriz)
    if matriz % 2 == 0:
        par += matriz
print('\n'*2)
print('\n')
print('='*50)
print(f'{"Matriz":^50}')
print('='*50)
print('\033[1;34m')
for d in dimen:
    print(f'[   {d[0]}  ] ', end='')
print('\n')
for e in dimen:
    print(f'[   {e[1]}  ] ', end='')
print('\n')
for f in dimen:
    print(f'[  {f[2]}   ] ', end='')
print('\n')
print('\033[1;30m='*50, end='')
print(f'{dimen[2][0]+dimen[2][1]+dimen[2][2]}')
#print(f'Maior valor da segunda linha é: {max(dimen[])}')
print(f'{par}')
