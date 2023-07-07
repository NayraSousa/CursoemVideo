n = int(input('Digite o número de termos: '))
n1 = 0
n2 = 1
print('{} - {}'.format(n1, n2), end='')
c = 3
while c <= n:
    n3 = n1 + n2
    print(' - {}'.format(n3), end='')
    c += 1
    n1 = n2
    n2 = n3





