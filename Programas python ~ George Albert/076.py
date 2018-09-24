from time import sleep
compras = ('Leite',7.0,
           'Biscoito',3.50,
            'Suco',2.87,
           'Laranja',2.0,
            'Frutas',6.0,
           'Massas',4.67,
            'Carnes',3.90,
           'Cerveja',15.0,
           'Guarana',3.0,
           'Sacos',0.4)
print('\033[1;36m='*57)
print('{:^57}'.format('MERCADÃO!!'))
print('='*57)
for i in range(0,len(compras)):
    if i % 2 == 0:
        print(f'{compras[i]:.<50}R$ ', end='')
        sleep(1)
    else:
        print(f'{compras[i]:.2f}')
        sleep(0.0)


