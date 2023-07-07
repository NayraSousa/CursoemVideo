pessoa18 = 0
homens = 0
mulheres20 = 0

continuar = 'S' or 'N'
while True:
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    genero = ' '
    while genero not in 'FfMm':
        genero = str(input('Qual o seu gênero? [F/M]: ')).strip().upper()
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? ]S/N]: ')).strip().upper()
    if idade > 18:
        pessoa18 += 1
    if genero == 'M':
        homens += 1
    if genero == 'F' and idade < 20:
        mulheres20 += 1
    if continuar == 'N':
        print(f'Foram cadastradas {pessoa18} maiores de 18 anos, {homens} homens e {mulheres20} mulheres menores de 20 anos.')
        break

