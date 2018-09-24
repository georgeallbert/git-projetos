vogais = ('amigos',
          'deus',
          'anjos',
          'familia',
          'dinheiro',
          'felicidade',
          'saude',
          'vide',
          'universo',
          'mundo')
for c in vogais:
    print(f'\nAs vogais de {c.upper()} são: ', end='')
    for d in c:
        if d.lower() in 'aeiou':
            print(d.upper(), end=' ')
