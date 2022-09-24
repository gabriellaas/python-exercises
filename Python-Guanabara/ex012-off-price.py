cost = float(input('Digite o preço em reais: '))
off = cost - (cost * 0.05)
print('O novo preço é R${:.2f}.'.format(off))

# forma resumida:
cost = float(input('Digite o preço em reais: '))
print('O novo preço é R${:.2f}.'.format(cost - (cost * 0.05)))

# valor do desconto personalizado:
cost = float(input('Digite o preço em reais: '))
off = int(input('Digite a % de desconto: '))
print('O novo preço é R${:.2f}.'.format(cost - (cost * (off/100))))
