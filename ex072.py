num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Escreva um número de 0 a 20: '))
while not numero < 0 and numero > 20:
    numero = int(input('Tente novamente! Escreva um número de 0 a 20: '))
print(num[numero])
