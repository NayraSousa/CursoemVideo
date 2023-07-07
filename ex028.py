import random
from time import sleep
num = int(input('Digite um número de 0 a 5: '))
y = [0, 1, 2, 3, 4, 5]
x = random.choice(y)
print('PROCESSANDO...')
sleep(2)
if num == x:
    print('Parabéns! Você acertou')
else:
    print('Sinto muito! Você errou')
print('Seu número: {}\nNúmero do pc: {}'.format(num, x))






