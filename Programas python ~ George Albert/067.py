print('\033[1;34m→'*50)
print('{TABUADA!}')
print('→'*50)
while True:
    n = int(input('\033[1;34mQual a tabuada: '))
    print('→'*50)
    if n == 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('→'*50)
