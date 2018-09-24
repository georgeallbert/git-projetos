resposta = ('Zero','Um','dois','três','quatro',
            'cinco','seis','sete','oito','nove',
            'dez','onze','doze','treze','quartoze',
            'quinze','dezeseis','dezesete','dezoito',
            'dezenove','vinte')
while True:
    pergunta = int(input('Digite um número entre 0 e 20: '))
    if 0 <= pergunta <= 20:
        break
    print('Erro 404 not found, ', end='')
print(f'\nO número digitado por extenso é {resposta[pergunta]}')

