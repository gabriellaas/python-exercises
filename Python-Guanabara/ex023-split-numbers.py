num = int(input('Digite um número entre 0 e 9999: '))
print('Unidade: {}'.format(num // 1 % 10))
print('Dezena: {}'.format(num // 10 % 10))
print('Centena: {}'.format(num // 100 % 10))
print('Milhar: {}'.format(num // 1000 % 10))

# mostra na tela cada um dos dígitos separadamente
