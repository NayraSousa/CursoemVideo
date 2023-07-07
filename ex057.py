g = ''
r = 's'
while g != 'M' and g != 'F':
    g = str(input('Digite o gênero [F/M]: ')).strip().upper()
    if g == 'F':
        print('Você é uma mulher!')
    elif g == 'M':
        print('Você é um homem!')
    else:
        r = input('Digite novamente!')
























