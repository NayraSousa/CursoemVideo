import math
x = int(input('Informe o ângulo: '))
cos = math.cos(math.radians(x))
sen = math.sin(math.radians(x))
tg = math.tan(math.radians(x))
print('O ângulo {} tem como cosseno, seno e tangente, respectivamente, {:.2f}, {:.2f}, {:.2f}'.format(x, cos, sen, tg))



