import random
from time import sleep
x = ''
y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
r = random.choice(y)
print('Tente adivinhar em qual número estou pensando...')
while x != r:
    x = int(input('Digite um número: '))
    sleep(1)
    soma += 1
    print('O número que você escolheu foi {}.'.format(x))
    if x == r:
        print('PARABÉNS!!')
        print('Você deu {} palpites'.format(soma))
    else:
        print('ERROU.')








