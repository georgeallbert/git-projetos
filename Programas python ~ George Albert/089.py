from operator import itemgetter
from random import randint
from time import sleep
print('\033[1;30m')
print('=' * 50)
print(f'{"SORTEIOS":^50}')
print('=' * 50)
dados = dict()
ordem = dict()
dados['1'] = randint(1,6)
dados['2'] = randint(1,6)
dados['3'] = randint(1,6)
dados['4'] = randint(1,6)
for n,v in dados.items():
    a = (f'|O jogador {n} >>> sorteou {v}|')
    b = a.center(50)
    print(b)
    sleep(1)
print('='*50)
a = ''' \033[1;36m
        ░░░░░░░░▄▄▄███░░░░░░░░░░░░░░░░░░░░
        ░░░▄▄██████████░░░░░░░░░░░░░░░░░░░
        ░███████████████░░░░░░░░░░░░░░░░░░
        ░▀███████████████░░░░░▄▄▄░░░░░░░░░
        ░░░███████████████▄███▀▀▀░░░░░░░░░
        ░░░░███████████████▄▄░░░░░░░░░░░░░
        ░░░░▄████████▀▀▄▄▄▄▄░▀░░░░░░░░░░░░
        ▄███████▀█▄▀█▄░░█░▀▀▀░█░░▄▄░░░░░░░
        ▀▀░░░██▄█▄░░▀█░░▄███████▄█▀░░░▄░░░
        ░░░░░█░█▀▄▄▀▄▀░█▀▀▀█▀▄▄▀░░░░░░▄░▄█
        ░░░░░█░█░░▀▀▄▄█▀░█▀▀░░█░░░░░░░▀██░
        ░░░░░▀█▄░░░░░░░░░░░░░▄▀░░░░░░▄██░░
        ░░░░░░▀█▄▄░░░░░░░░▄▄█░░░░░░▄▀░░█░░
        ░░░░░░░░░▀███▀▀████▄██▄▄░░▄▀░░░░░░
        ░░░░░░░░░░░█▄▀██▀██▀▄█▄░▀▀░░░░░░░░
        ░░░░░░░░░░░██░▀█▄█░█▀░▀▄░░░░░░░░░░
        ░░░░░░░░░░█░█▄░░▀█▄▄▄░░█░░░░░░░░░░
        ░░░░░░░░░░█▀██▀▀▀▀░█▄░░░░░░░░░░░░░
        ░░░░░░░░░░░░▀░░░░░░░░░░░▀░░░░░░░░░\033[m\033[1;30m'''
c = a.center(50)
print(c)
print('='*50)
print(f'{"LUGARES DOS JOGADORES":^50}')
ordem = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('='*50)
for x,y in enumerate(ordem):
    z = (f'|{x}º colocadoo >>> sorteou {y[1]}|')
    q = z.center(50)
    print(q)
    sleep(1)
print('='*50)
