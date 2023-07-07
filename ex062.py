a = float(input('Qual o primeiro termo? '))
r = float(input('Qual a razão? '))
n = 1
t = ''
while n < 11:
    an = a + (n - 1) * r
    n += 1
    print(an)
while t != 0:
    t = int(input('Você quer mostrar mais algum termo? '))
    pa = a + (t - 1) * r
    print(pa)
print('Programa finalizado!')
