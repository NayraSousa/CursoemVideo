from time import sleep
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('PROCESSANDO...')
sleep(2)
print('O imc da pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso!')
if imc >= 18.5 and imc < 25:
    print('Peso ideal.')
if imc >= 25 and imc < 30:
    print('Sobrepeso.')
if imc >= 30 and imc < 40:
    print('Obesidade.')
if imc > 40:
    print('Obesidade mórbida.')




