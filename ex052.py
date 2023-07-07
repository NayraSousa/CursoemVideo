'''num = int(input('Digite um número: '))
if num // num == 1 and num // 1 == num and num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
    print('É um número primo!')
else:
    print('NÃO é um número primo!')'''
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
if tot == 2:
    print('É primo!')
else:
    print('Não é primo!')










