prod = float(input('Digite o valor do produto: '))
pag = int(input(' 1 - Dinheiro ou cheque\n 2 - Á vista no cartao\n 3 - No cartão em 2x\n 4 - No cartão em 3x\n '
                'Digite o número da forma de pagamento desejado: '))
if pag == 1:
    print('Você tem 10% de desconto. O valor do produto sairá por {} reais'.format(prod * 0.9))
elif pag == 2:
    print('Você tem 5% de desconto. O valor do produto sairá por {} reais'.format(prod * 0.95))
elif pag == 3:
    print('O produto sai no valor normal. Custando {} reais'.format(prod))
elif pag == 4:
    print('Será cobrado 20% de juros. E o produto sairá por {} reais'.format(prod * 1.2))
else:
    print('Essa opção não existe')






