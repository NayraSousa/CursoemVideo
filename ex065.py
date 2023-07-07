opcao = ''
soma = 0
dig = 0
maiorvalor = 0
menorvalor = 0
while opcao != 'N':
    num = (int(input('Digite um número: ')))
    dig += 1
    soma += num
    media = soma / dig
    if dig == 1:
        maiorvalor = num
        menorvalor = num
    else:
        if num > maiorvalor:
            maiorvalor = num
        if num < menorvalor:
            menorvalor = num
    opcao = str(input('Quer continuar? [S/N]: ')).upper()
print('Programa finalizado! A média entre os números é {}, o maior valor é {} e o menor valor é {}.'.format(media, maiorvalor, menorvalor))


