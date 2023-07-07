dist = float(input('Qual a distância da viagem em quilômetros? '))
x = dist * 0.50
y = dist * 0.45
if dist <= 200:
    print('O valor da viagem será: {}'.format(x))
else:
    print('O valor da viagem será: {}'.format(y))


