soma = 0
idademaiorhomem = 0
nomemaisvelho = ''
totmulher = 0
for q in range(1, 5):
    print('--- {}ª PESSOA ---'.format(q))
    nome = str(input('Qual o seu nome? ')).strip()
    idade = int(input('Qual a sua idade? '))
    genero = str(input('Qual o seu gênero? [F/M] ')).strip()
    soma += idade
    if genero in 'Mm' and idade > idademaiorhomem:
        idademaiorhomem = idade
        nomemaisvelho = nome
    if genero in 'fF' and idade < 20:
        totmulher += 1
print('A média entre as idade é: {}.'.format(soma/4))
print('A idade do homem mais velho é {} e o nome dele é {}'.format(idademaiorhomem, nomemaisvelho))
print('O total de mulheres com a idade menor do que 20 é {}'.format(totmulher))









