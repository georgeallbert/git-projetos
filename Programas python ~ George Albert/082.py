print('\033[1;30m')
print('='*50)
print(f'{"084":^50}')
print('='*50)
nome = list()
resolu = list()
mais = menos = cont = 0
nome_menor = ' '
nome_maior = ' '
while True:
    print('\033[1;30m')
    nome.append(str(input('Nome: ')))
    cont +=1
    nome.append(int(input('Peso: ')))
    if len(resolu) == 0:
        mais = menos = nome[1]
        nome_menor = nome_maior = nome[0]
    else:
        if nome[1] > mais:
            mais = nome[1]
            nome_maior = nome[0]
        if nome[1] < menos:
            menos = nome[1]
            nome_menor = nome[0]
    resolu.append(nome[:])
    nome.clear()
    continuar = str(input('Deseja prosseguir? [Yes/not] ')).upper().strip()[0]
    while continuar not in 'YN':
        print('\033[1;31m')
        continuar = str(input('[Yes/not]: ')).upper().strip()[0]
        print('\033[m')
    if continuar == 'N':
        break

print('\n'*100)
print('='*50)
print(f'{"QUANTIDADE DE PESSOAS!":^50}')
print('='*50)
print(f'Você cadastrou {cont:.>30} pesos')
print('='*50)
print('='*50)
print(f'{"Pessoas e seus relativos pesos":^50}')
print('='*50)
for n in resolu:
    print(f'{n[0]:.<30} {n[1]}kg')
print('='*50)
print('\n')
print('='*50)
print(f'{"Maiores":^50}')
print('='*50)
for gr in resolu:
    if gr[1] > menos:
        print(f'Maior peso: {gr[0]:.<30} {gr[1]}kg ', end='')
        print()
print('='*50)
print(f'{"Menore!":^50}')
print('='*50)
for pn in resolu:
    if pn[1] <= menos:
        print(f'Menor peso: {pn[0]:.<30} {pn[1]}kg')
print('='*50)



