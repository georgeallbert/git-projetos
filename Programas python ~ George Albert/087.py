from random import sample
lista = list()
jogos = list()
print('\033[1;30m')
print('='*50)
print(f'{"MEGA SENA":^50}')
print('='*50)
r = int(input('Jogos a serem gerados: '))
for j in range(1,r +1):
    jogo = sample(range(1,61),6)
    jogos.append(jogo)
    lista.append(jogos[:])
    jogos.clear()
    print(f'{lista}')

