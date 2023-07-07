sal = float(input('Digite seu salário: '))
x = sal * 0.1
x1 = sal * 1.10
y = sal * 0.15
y1 = sal * 1.15
if sal > 1250:
    print('Você terá um aumento de {:.1f} e ganhará {:.1f}'.format(x, x1))
if sal <= 1250:
    print('Você terá um aumento de {:.1f} e ganhará {:.1f}'.format(y, y1))
