'''nome = str(input('Digite seu nome: '))
idade = int(input('Digite a sua idade: '))
if idade <= 9:
    print('Olá, {}. A sua categoria é MIRIM.'.format(nome))
if idade > 9 and idade <= 14:
    print('Olá, {}. A sua categoria é INFANTIL.'.format(nome))
if idade > 14 and idade <= 19:
    print('Olá, {}. A sua categoria é JUNIOR.'.format(nome))
if idade > 19 and idade <= 20:
    print('Olá, {}. A sua categoria é SÊNIOR.'.format(nome))
if idade > 20:
    print('Olá, {}. A sua categoria é MASTER.'.format(nome))'''
from datetime import date
atual = date.today().year
ano = int(input('Qual o ano do seu nascimento? '))
idade = atual - ano
if idade <= 9:
    print('Você tem {} anos e a sua classificação é MIRIM.'.format(idade))
if idade > 9 and idade <= 14:
    print('Você tem {} anos e a sua classificação é INFANTIL.'.format(idade))
if idade > 14 and idade <= 19:
    print('Você tem {} anos e a sua classificação é JÚNIOR.'.format(idade))
if idade > 19 and idade <= 25:
    print('Você tem {} anos e a sua classificação é SÊNIOR.'.format(idade))
if idade > 25:
    print('Você tem {} anos e a sua classificação é MASTER.'.format(idade))


