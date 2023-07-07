p = 0
m = 0
maisbarato = 0
maiscaro = 0
c = 0
barato = 0
while True:
    prod = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    p += preco
    c += 1
    if preco > 1000:
        m += 1
    if c == 1:
        maisbarato = preco
        maiscaro = preco
        barato = prod
    if preco > maiscaro:
        maiscaro = preco
    if preco < maisbarato:
        maisbarato = preco
        barato = prod
    if continuar == 'N':
        print(f'O total das compras é {p} reais.\n{m} produtos custam mais de R$1000,00.\nO produto mais barato é {barato}.')
        break



