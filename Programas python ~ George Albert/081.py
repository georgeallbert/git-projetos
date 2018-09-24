print('\033[1;30m='*100)
print(f'{"HASTEIN ANONYK":^100}')
print('='*100)
n = list()
p = list()
i = list()
cont = 0
todos = 0
while True:
    valor = int(input('\nDigite um valor: '))
    n.append(valor)
    todos +=1
    if valor % 2 == 0:
        print('\n\033[1;34mVALOR PAR ADCIONADO!\033[m ')
        p.append(valor)
        cont +=1
    else:
        print('\n\033[1;32mVALOR ÍMPAR ADCIONADO!\033[m ')
        i.append(valor)
    continuar = str(input('\n\033[1;30mDeseja continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('\n\033[1;31mDigite novamente, [S/N]:\033[m\033[1;30m ')).strip().upper()[0]
    if continuar == 'N':
        break
print('='*100)
print(f'{"VALORES!":^100}')
print('='*100)
if todos > 1:
    k = min(n)
    n.sort(reverse=True)
    print('\n\033[1;30mTodos os \033[1;36m[VALORES]\033[m \033[1;30mdigitados:\033[m \033[1;30m: ', end='')
    for a in n:
        print(f'[{a}]', end='')
        print(' = FIM ' if k == a else ' ⇜⇝ ', end='')
else:
    print(f'\n\nO unico valor \033[1;34m[DIGITADO]: {n} = FIM\033[m \033[1;30m')
if cont > 1:
    n = min(p)
    p.sort(reverse=True)
    print('\n\nValores \033[1;33m[PARES] \033[m \033[1;30mdigitados: ', end='')
    for r in p:
        print(f'[{r}]', end='')
        print(' = FIM ' if n == r else ' ⇜⇝ ', end='')
elif cont == 0:
    print('\n\nNenhum valor \033[1;31m[PAR]\033[m \033[1;30mdigitado!')
elif cont == 1:
    print('\n\nUnico valor que é \033[1;35m[PAR]:\033[m \033[1;30m', end='')
    for b in p:
        print(f'[{b}] = FIM ', end='')
if valor not in i:
    print('\n\nNenhum valor \033[1;31m[ÍMPAR]\033[m \033[1;30mdigitado')
else:
    i.sort(reverse=True)
    x = min(i)
    print('\n\nValores que são \033[1;32m[ÍMPARES]\033[m:\033[1;30m ', end='')
    for c in i:
        print(f'[{c}]', end='')
        print(' = FIM' if x == c else ' ⇜⇝ ',end='')
