f = ('\n'*100)
meio = ('='*70)
a = meio.center(50,)
print('\033[1;30m')
print(a)
print(f'{"VERSALA":^50}')
print(a)
notas = list()
cont = 0
quanto = int(input('Por quanto a escola divide a media: '))
while True:
    alunos = str(input('Nome do aluno(a): '))
    nota1 = float(input(f'Nota do teste do aluno {alunos}: '))
    nota2 = float(input(f'Nota da prova do aluno {alunos}: '))
    nota3 = float(input(f'Nota dos trabalhos do aluno {alunos}: '))
    nota4 = float(input(f'Nota de comportamento do aluno {alunos}: '))
    media = nota1 + nota2 + nota3 + nota4
    total = media / quanto
    notas.append([alunos, total])
    continuar = str(input('Cadastrar mais alunos? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('\033[1;31mDigite novamente? [S/N]:\033[m\033[1;30m ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f)
print(a)
print(f'{"BOLETIM":^50}')
print(a)
print(a)
print('Pos', end='')
print(f'{"Nome":^43}', end='')
print(f'{"Media":^30}', end='')
print()
print(a)
for n, v in enumerate(notas):
    print(f'{n} {v[0]:^43} {v[1]:^30}')
print(a)
while True:
    novamente = int(input('Mostrar nota de qual aluno? [999-SAIR]: '))
    if novamente == 999:
        break
    elif novamente <= len(notas)-1:
        print(a)
        print(f'{novamente} {notas[novamente][0]:^43} {notas[novamente][1]:^30}')
        print(a)
