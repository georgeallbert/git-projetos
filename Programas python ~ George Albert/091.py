from operator import itemgetter
print('\033[1;30m')
print('='*70)
print(f'{"Odeio futebol":^70}')
print('='*70)
total = 0
jogos = dict()
nome = dict()
ordem = list()
nome['nome'] = str(input('Nome do jogador: '))
print('='*70)
for c in range(0,5):
    jogos[c] = int(input(f'|Qual foi o saldo de gols do jogador {nome["nome"]} na partida {c}: |'))
    total += jogos[c]
ordem = sorted(jogos.items(), key=itemgetter(1))
print('='*70)
print(f'=> O jogador {nome["nome"]}')
print(f'=> O jogador {nome["nome"]} tem o saldo de gols igual a: ', end='')
for j in ordem:
    print(f' [{j[1]}] <=> ', end='')
print(' = FIM', end='')
print()
print(f'=> O total de gols é igual a {total}')
print(f'=> O jogador {nome["nome"]} jogou 5 partidas')
print('='*70)
for v, n in jogos.items():
    print(f'=> Na partia {v+1}, o jogador {nome["nome"]} fez {n} gols')
print('='*70)
print('''\033[1;31m
░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄
░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄
░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█
░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█
░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█
█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█
█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
░░░█░░██░░▀█▄▄▄█▄▄█▄████░█
░░░░█░░░▀▀▄░█░░░█░███████░█
░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█''')


