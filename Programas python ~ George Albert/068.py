from random import randint
v = 0
while True:
    n = int(input('\n\033[1;31mDigite um valor: '))
    comp = randint(0, 10)
    total = comp + n
    tipo = ' '
    while tipo not in 'iIPp':
        tipo = str(input('Par ou Impar [P/I]')).strip().upper()[0]
    print(f'\nVocê jogou = {n}\n\ncomputador jogou = {comp}\n\ntotal = {total}')
    if tipo == 'P':
        if total % 2 == 0:
            v +=1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break
print(f'Você venceu {v}')





