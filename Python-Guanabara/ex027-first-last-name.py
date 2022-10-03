name = str(input('Digite seu nome completo: ')).strip()
nm = name.split()
print('Seu primeiro nome é {}.'.format(nm[0]))
print('Seu último nome é {}.'.format(nm[len(nm) - 1]))
