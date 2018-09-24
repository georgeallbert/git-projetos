from time import sleep
print('\033[1;30m')
print('='*50)
print(f'{"Cadatros":^50}')
print('='*50)
cadastro = dict()
feminino = list()
acima = list()
cont = total = 0
while True:
    cadastro['nome'] = str(input(' =>  Nome:             | '))
    sleep(1)
    cont += 1
    cadastro['idade'] = int(input(' =>  Idade:            | '))
    sleep(1)
    total += cadastro['idade']
    cadastro['sexo'] = str(input(' =>  Sexo [F/m]:       | ')).lower().strip()[0]
    sleep(1)
    while cadastro['sexo'] not in 'fm':
        cadastro['sexo'] = str(input('=> Sexo? [M/f]:    | ')).lower().strip()[0]
        sleep(1)
    if cadastro['sexo'] == 'f':
        feminino = cadastro['nome']
    if cadastro['idade'] >= 18:
        acima.append(cadastro.copy())
        cadastro.clear()
    continuar = str(input(' =>  Continuar? [S/n]: | ')).lower().strip()[0]
    sleep(1)
    while continuar not in 'sn':
        continuar = str(input(' => Outra vez! Continuar? [S/n]: ')).lower().strip()[0]
        sleep(1)
    print('='*50)
    if continuar == 'n':
        break
print(f'| => {cont} pessoas cadastradas                              ')
sleep(1)
print(f'| => media de todos os cadatrados é igual a: {total}        ')
sleep(1)
for v in acima:
    print(f'| => Acima da media: {v}       ')
    sleep(1)
sleep(1)
print('| => Mulheres: ', end='')
for f, v in enumerate(feminino):
    print(f'{v}', end='')
print()
print('='*50)
print('\n'*5)
sleep(1)
print(f'{"E":^150}')
sleep(1)
print(f'{"N":^150}')
sleep(1)
print(f'{"C":^150}')
sleep(1)
print(f'{"E":^150}')
sleep(1)
print(f'{"R":^150}')
sleep(1)
print(f'{"R":^150}')
sleep(1)
print(f'{"A":^150}')
sleep(1)
print(f'{"D":^150}')
sleep(1)
print(f'{"O":^150}')
sleep(1)




