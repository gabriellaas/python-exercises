dias = int(input('Quantidade de dias? '))
km = float(input('Quantidade de km rodados? '))
total = 60 * dias + (0.15 * km)
print('O preço a pagar é: R${:.2f}.'.format(total))
