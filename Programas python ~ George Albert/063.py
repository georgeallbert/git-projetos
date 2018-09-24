print('→'*50)
print('Sequência de fibonati!')
print('→'*50)
n = int(input('Digite uma sequência: '))
print('→'*50)
t1 = 0
t2 = 1
print('{} → {} '.format(t1, t2), end='')
total = 3
loop = 0
nuvo = 1
while total <= n:
    t3 = t1 + t2
    print('→ {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    total += 1
print('Fim')

