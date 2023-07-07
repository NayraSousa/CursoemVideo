import random
jogo = 'PAR' or 'IMPAR'
print('='*20)
print('PAR OU ÍMPAR?')
print('='*20)
num = num1 = int(input('Digite um valor de 0 a 10: '))
opcao = opcao1 = str(input('PAR OU ÍMPAR? ')).upper().strip()
y = random.randint(0, 10)
soma = num + y
vitoria = 0
while True:
    y = random.randint(0, 10)
    soma1 = num1 + y
    if soma1 % 2 == 0:
        jogo = 'PAR'
    else:
        jogo = 'IMPAR'
    if jogo == opcao1:
        print(f'Você ganhou! O número que você escolheu foi {num1}, o número que a máquina escolheu foi {y} e a soma deu {soma1}, então deu {jogo}.')
        num1 = int(input('Digite um valor de 0 a 10: '))
        opcao1 = str(input('PAR OU ÍMPAR? ')).upper().strip()
        vitoria += 1
    elif jogo != opcao1:
        print(f'Você perdeu! O número que você escolheu foi {num1}, o número que a máquina escolheu foi {y} e a soma deu {soma1}, então deu {jogo}\nVocê teve {vitoria} vitórias.')
        break














