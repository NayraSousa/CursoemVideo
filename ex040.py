n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
if média < 5:
    print('REPROVADO! Sua nota foi {:.1f}'.format(média))
if média >= 5 and média <= 6.9:
    print('RECUPERAÇÃO. Sua nota foi {:.1f}'.format(média))
if média >= 7:
    print('APROVADO. Sua nota foi {:.1f}'.format(média))






