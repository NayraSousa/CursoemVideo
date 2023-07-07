from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('PROCESSANDO...')
sleep(2)
if n1 > n2:
    print('O primeiro valor é maior!')
elif n1 < n2:
    print('O segundo valor é maior!')
elif n1 == n2:
    print('O primeiro e o segundo valor são iguais!')

