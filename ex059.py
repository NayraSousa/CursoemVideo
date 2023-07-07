opcao = 0
valor1 = float(input('Digite o 1° valor: '))
valor2 = float(input('Digite o 2° valor: '))
while opcao != 5:
    opcao = int(input('[1] - SOMA\n[2] - MULTIPLICAÇÃO\n[3] - MAIOR VALOR\n[4] - NOVOS NÚMEROS\n[5] - SAIR\nESCOLHA UMA OPÇÃO: '))
    if opcao == 1:
        print('A soma dos valores é igual a {}.'.format(valor1 + valor2))
    if opcao == 2:
        print('A multiplicação entre os valores é {}.'.format(valor1 * valor2))
    if opcao == 3:
        if valor1 == valor2:
            print('Os valores são iguais!')
        elif valor1 > valor2:
            print('O maior valor é {}.'.format(valor1))
        else:
            print('O maior valor é {}.'.format(valor2))
    if opcao == 4:
        valor1 = float(input('Digite o 1° valor: '))
        valor2 = float(input('Digite o 2° valor: '))
    if opcao == 5:
        print('Programa finalizado!')
    if opcao > 5:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE')























