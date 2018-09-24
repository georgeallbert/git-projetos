print('='*50)
print('{:^50}'.format('BANCO ITAU'))
print('='*50)
valor = int(input('Valor para sacar: R$ '))
total = valor
céd = 100
totalcéd = 0
while True:
    if total >= céd:
        total -= céd
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f'\n{totalcéd} cédula de {céd}')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 2
        totalcéd = 0
        if total == 0:
            break

