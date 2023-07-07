nome = str(input('Qual o seu nome? '))
casa = float(input('Qual o valor da casa que deseja? '))
salário = float(input('Quanto você ganha mensalmente? '))
ano = float(input('Quantos anos pretende passar pagando?'))
pm = casa / (ano * 12)
print('O valor da parcela fica {:.2f}'.format(pm))
if pm > 0.3 * salário:
    print('Empréstimo negado!')
else:
    print('Você pode concluir a sua compra!')

    
