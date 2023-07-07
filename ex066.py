soma = quant = 0
while True:
    num = int(input('Digite um número [999 finaliza o programa] : '))
    if num == 999:
        break
    soma += num
    quant += 1
print(f'Programa finalizado! A quantidade de números lidos foi {quant} e a soma dos números é {soma}')

