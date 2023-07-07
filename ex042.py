r1 = float(input('Digite a primeira medida: '))
r2 = float(input('Digite a segunda medida: '))
r3 = float(input('Digite a terceira medida: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Forma um triângulo!')
    if r1 == r2 == r3:
        print('É um triângulo equilátero!')
    if r1 == r2 and r2 != r3 or r1 == r3 and r3 != r2 or r2 == r3 and r3 != r1:
        print('É um triângulo isósceles!')
    if r1 != r2 and r1 != r3 and r2 != r3:
        print('É um triângulo escaleno!')
else:
    print('Não forma um triângulo!')


