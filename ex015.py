km = float(input('Quantos quilômetros percorridos? '))
dias = int(input('Quantos dias você usou? '))
preço = (0.15 * km) + 60 * dias
print('Você rodou {} quilômetros em {} dias e precisará pagar {:.2f} reais.'.format(km, dias, preço))
