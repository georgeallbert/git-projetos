print('\033[1;30m')
print('='*50)
print(f'{"ODEIO FUTEBOL!":^50}')
print('='*50)
futebol = dict()
jogos = list()
gols = list()
cont = 0
while True:
    futebol['jogador'] = str(input('=> Nome do jogador: '))
    partidas = int(input(f'=> Quantas partidas o jogador {futebol["jogador"]} jogou? '))
    print('='*50)
    for c in range(0, partidas +1):
        gols.append(int(input(f'=> Quantos gols na partida {c}: ')))
    futebol['gols'] = gols[:]
    #cont += sum(gols)
    gols.clear()
    jogos.append(futebol.copy())
    print('='*50)
    continuar = str(input('=> Continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('=> Não entendi! Continuar? [S/N]: '))
    print('='*50)
    if continuar == 'N':
        break
for numeros in futebol['gols']:
    cont += numeros
print(f'{"Psº"}', end='')
print(f'{"NOME":>15}', end='')
print(f'{"GOLS":>15}', end='')
print(f'{"TOTAL":>15}', end='')
print()
print('='*50)
for i in range(len(jogos)):
    print(f'{i} {jogos[i]["jogador"]:>17} {str(futebol["gols"]):>15} {str(cont):^17}')
print('='*50)
while True:
    dados = str(input('Mostrar dados de qual jogador? [999\P~/Sair]'))
    if dados == 999:
        break
    while True:
        for k, v in range(len(jogos)):
            print(f'No jogo {k} fez {str(futebol["gols"]} gols')



