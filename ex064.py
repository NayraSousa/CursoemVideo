num = 0
soma = 0
dig = 0
while num != 999:
    soma += num
    num = int(input('Digite um número: '))
    dig += 1
print('Programa encerrado!\nVocê digitou {} números e a soma entre eles é {}'.format((dig - 1), soma))




