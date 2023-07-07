from datetime import date
atual = date.today().year
s = 0
b = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade <= 20:
        s += 1
    else:
        b += 1
print('No total são {} MENORES de idade e {} pessoas MAIORES de idade.'.format(s, b))


















