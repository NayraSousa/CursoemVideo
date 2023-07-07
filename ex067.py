while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} * {c} = {num * c}')
print('PROGRAMA FINALIZADO.')

