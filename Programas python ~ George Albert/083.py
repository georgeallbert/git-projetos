print('\033[1;30m')
n = [], []
valor = True
for c in range(1, 8):
    valor = int(input('Valor: '))
    print('\n'*50)
    if valor % 2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
n[0].sort()
n[1].sort()
g = max(n[0])
h = max(n[1])
print('Valores pares: ', end='')
for a in n[0]:
    print(f'[{a}] ', end='')
    print('= FIM'if a == g else '= ',end='')
print('\n'*2)
print('Valores ímpares: ', end='')
for b in n[1]:
    print(f'[{b}] ',end='')
    print('= FIM'if b == h else '= ',end='')
