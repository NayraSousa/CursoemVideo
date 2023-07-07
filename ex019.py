import random
a = str(input('Digite um nome: '))
b = str(input('Digite um nome: '))
c = str(input('Digite um nome: '))
d = str(input('Digite um nome: '))
alunos = [a, b, c, d]
x = random.choice(alunos)
print('O aluno escolhido foi {}'.format(x))


