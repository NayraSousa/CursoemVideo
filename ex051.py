a1 = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão? '))
for c in range(1, 11):
    print('an = {} + ({} - 1) * {} = {}'.format(a1, c, r, a1 + (c - 1) * r))







