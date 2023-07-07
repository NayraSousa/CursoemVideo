import random
from time import sleep
part = int(input('1 - pedra\n2 - papel\n3 - tesoura\nDigite o número da opção desejada: '))
y = [1, 2, 3]
x = random.choice(y)
print('PROCESSANDO...')
sleep(2)
if part == x:
    print('EMPATE')
if x == 1 and part == 2:
    print('PARABÉNS! VOCÊ GANHOU.')
if x == 1 and part == 3:
    print('QUE PENA! VOCÊ PERDEU.')
if x == 2 and part == 1:
    print('QUE PENA! VOCÊ PERDEU.')
if x == 2 and part == 3:
    print('PARABÉNS! VOCÊ GANHOU.')
if x == 3 and part == 1:
    print('PARABÉNS! VOCÊ GANHOU.')
if x == 3 and part == 2:
    print('QUE PENA! VOCÊ PERDEU')
print('A máquina escolheu {}'.format(x))






