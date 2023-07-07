km = int(input('Digite a velocidade em km/h: '))
x = (km - 80) * 7
if km > 80:
    print('Você foi multado por andar a {}km/h. O valor da sua multa será: {}'.format(km, x))
else:
    print('Tudo sob controle. Tenha um bom dia!')



