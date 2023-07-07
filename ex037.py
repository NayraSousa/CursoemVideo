n = int(input('Digite o número o qual deseja converter: '))
n2 = int(input('Digite 1 para converter para binário\nDigite 2 para converter para octal\nDigite 3 para converter para hexadecimal: '))
if n2 == 1:
    print(bin(n)[2:])
elif n2 == 2:
    print(oct(n)[2:])
elif n2 == 3:
    print(hex(n)[2:])
else:
    print('Opção inválida')



