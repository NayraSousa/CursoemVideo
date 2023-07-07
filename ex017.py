from math import sqrt
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = co ** 2 + ca ** 2
print('O valor da hipotenusa é {:.2f}'.format(sqrt(h)))

