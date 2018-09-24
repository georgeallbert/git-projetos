print('\n{:=^50}'.format('AS COMPRAS'))
total = totalmil = menor = mil = maior = cont = 0
barato = ' '
caro = ' '
while True:
    produto = str(input('\nPRODUTO: '))
    preço = float(input('\nPREÇO: R$ '))
    cont += 1
    mil += preço
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    if preço > maior:
        maior = preço
        caro = produto
    if preço == 1000 or preço > 1000:
        totalmil += 1
    continuar = ' '
    while continuar not in 'SNYEXIT':
        continuar = str(input('\nDeseja continuar? [S/N/Y/EXIT]: ')).upper().strip()[0]
    if continuar == 'E' or continuar == 'N':
        break
print(f'\nO total gasto foi de {mil}')
print(f'\n{totalmil} Produtos maiores que mil')
print(f'\nO produto mais barato foi {barato} que custa {menor}')
print(f'\nO produto mais caro foi {caro} que custa {maior}')
print(f'\nO Você comprou {cont} produtos')

