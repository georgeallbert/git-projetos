print('='*50)
print(f'\033[1;30m{"INSS":^50}')
print('='*50)
from datetime import date
date_atual = date.today().year

trabalho = dict()
while True:
    trabalho['nome'] = str(input('Nome do(a) trabalhador(a): '))
    trabalho['nascimento'] = int(input(f'\nData de nascimento do(a) trabalhador(a), {trabalho["nome"]}: '))
    trabalho['sem_carteira'] = date_atual - trabalho['nascimento']
    tempo = int(input(f'\nTempo na empresa, sr(a) {trabalho["nome"]}: '))
    proceguir = str(input('\nTem carteira de trabalho? [S/N]: ')).upper().strip()[0]
    while proceguir not in 'SN':
        proceguir = str(input('\nOutra vez! Tem carteira de trabalho? [S/N]: ')).upper().strip()[0]
    if proceguir == 'S':
        trabalho['carteira'] = int(input(f'\nNº da carteira do(a) trabalhador(a) {trabalho["nome"]}: '))
        trabalho['contratação'] = tempo - date_atual
        trabalho['salario'] = float(input(f'\nSalário do trabalhador(a) {trabalho["nome"]}: '))
        trabalho['aposentadoria'] = date_atual - trabalho['nascimento'] + tempo
        ta = (f'Nome do trabalhador >>> {trabalho["nome"]}')
        te = ta.center(145)
        tp = (f'Idade do trabalhador >>> {trabalho["sem_carteira"]}')
        to = tp.center(143)
        tn = (f'   Nº da carteira do trabalhador >>> {trabalho["carteira"]}')
        tc = tn.center(149)
        tt = (f'       Data de contratação do trabalhador >>> {trabalho["contratação"]}')
        tl = tt.center(149)
        ts = (f'Salário do trabalhador >>> {trabalho["salario"]}')
        tz = ts.center(147)
        tf = (f'Idade a se aposentar >>> {trabalho["aposentadoria"]}')
        tg = tf.center(144)
        yu = ('='*50)
        yo = yu.center(150)
        print('\n'*30)
        print(yo)
        print(f'{"DADOS":^150}')
        print(yo)
        print(te)
        print(to)
        print(tc)
        print(tl)
        print(tz)
        print(tg)
        print(yo)
        print('\n'*18)
        break
    else:
        print('\n'*30)
        ff = (f'|Nome do trabalhador >>> {trabalho["nome"]}')
        fa = ff.center(144)
        fv = (f'|Idade do trabalhador >>> {trabalho["sem_carteira"]}')
        ft = fv.center(142)
        fi = (f'|Nº da carteira: >>> Sem_carteira')
        fh = fi.center(147)
        fl = ('='*50)
        fk = fl.center(150)
        w = '''\033[1;31m
                                                        ____________________¶¶¶
                                                        _____________________¶
                                                        _____________________¶¶¶¶¶¶¶¶¶¶¶¶¶
                                                        _____________________¶¶¶___¶__¶_¶¶¶¶
                                                        _____________________¶¶¶___¶¶¶¶___¶¶
                                                        _____________________¶¶¶__¶¶¶¶¶___¶¶
                                                        _____________________¶¶¶__¶¶¶¶¶___¶
                                                        _____________________¶¶¶¶¶¶__¶¶___¶
                                                        _____________________¶_________¶¶¶¶
                                                        _____________¶¶¶¶¶¶¶¶¶¶¶¶¶
                                                        _____________¶¶___________¶¶
                                                        ______________¶____________¶
                                                        ______________¶_____________¶
                                                        _______________¶____________¶
                                                        _______________¶____________¶_¶¶
                                                        _______________¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
                                                        _____¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________¶
                                                        _____¶____________¶¶_____________¶¶____¶
                                                        _____¶¶____________¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
                                                        ______¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________¶
                                                        ______¶¶_____¶¶___________¶______________¶¶
                                                        _______¶______¶____________¶______________¶
                                                        _______¶______¶¶___________¶_____________¶¶
                                                        _______¶_______¶___________¶_____________¶¶
                                                        ______¶¶_______¶___________¶¶____________¶
                                                        ______¶¶¶¶¶¶¶¶¶¶¶__________¶¶___________¶¶
                                                        ___________¶_¶_¶¶________¶¶¶_____¶¶¶¶¶¶¶¶_____¶¶¶
                                                        ___________¶_¶_¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶_______¶¶¶¶¶__¶¶
                                                        ¶¶¶¶¶¶_____¶_¶______¶¶_¶_______¶_¶¶¶¶¶¶¶¶¶___¶¶¶¶¶
                                                        ¶¶___¶¶¶¶¶¶¶¶¶______¶¶_¶____¶¶¶¶¶¶¶________¶¶
                                                        __¶¶________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶______¶
                                                        ____¶____________________________¶¶_¶____¶
                                                        _____¶_____¶¶¶_____¶¶_____¶¶¶_____¶¶¶___¶¶
                                                        ______¶___¶¶_¶¶___¶¶_¶____¶_¶¶__________¶
                                                        ______¶¶____¶¶_____¶¶¶_____¶¶__________¶¶
                                                        _______¶¶_____________________________¶¶
                                                        ________¶¶___________________________¶¶
                                                        _________¶¶________________________¶¶¶
                                                        ___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶'''
        print('\033[1;30m')
        i = w.center(200)
        print(fk)
        print(f'{"SEM CARTEIRA":^150}')
        print(fk)
        print(fa)
        print(ft)
        print(fh)
        print(fk)
        print(i)
        print('\n'*18)
        break

    
