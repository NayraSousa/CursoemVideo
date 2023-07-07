valor1 = int(input('Digite um valor de 0 a 9: '))
valor2 = int(input('Digite um valor de 0 a 9: '))
valor3 = int(input('Digite um valor de 0 a 9: '))
valor4 = int(input('Digite um valor de 0 a 9: '))
valores = (valor1, valor2, valor3, valor4)
print(valores)
print(f'O número 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na posição {valores.index(3) + 1}')
else:
    print(f'O número 3 apareceu 0 vezes')
print('Os valores pares digitados foram', end=' ')
for x in valores:
    if x % 2 == 0:
        print(x, end=' ')







