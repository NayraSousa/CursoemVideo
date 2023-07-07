'''nome = input('Digite seu nome: ')
idade = float(input('Digite a sua idade: '))
menos = 18 - idade
mais = idade - 18
if idade == 18:
    print('Você já pode ir se alistar!')
elif idade < 18:
    print('Você ainda não tem idade para se alistar!')
    print('Ainda faltam {} anos para você poder se alistar'.format(menos))
elif idade > 18:
    print('Que irresponsável! Você está {} anos atrasado.'.format(mais))'''
from datetime import date
atual = date.today().year
nas = int(input('Qual ano você nasceu? '))
idade = atual - nas
menos = 18 - idade
mais = idade - 18
if idade < 18:
    print('Você ainda não tem idade para se alistar.')
    print('Faltam {} anos para você se alistar'.format(menos))
if idade > 18:
    print('Você já deveria ter se alistado!')
    print('Você está atrasado {} anos'.format(mais))
if idade == 18:
    print('Está na hora de se alistar! Dirija-se ao quartel mais próximo.')


