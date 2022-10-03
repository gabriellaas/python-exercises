name = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}.'.format(name.upper()))
print('Seu nome em minúsculas é {}.'.format(name.lower()))
print('Seu nome tem {} letras.'.format(len(name) - name.count(' ')))  # total de letras no nome sem contar espaços
firstName = name.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(firstName[0], name.find(' ')))

# count(' ') = conta a quantidade dos caracteres passados nos ()
# find(' ') = mostra o local onde começa
# len() = conta o total de letras
# lower = coloca tudo em minúscula
# lstrip = remove os espaços à esquerda
# rstrip = remove os espaços à direita
# split = divide o nome em lista através dos espaços
# strip = remove os espaços no início e no final da string
# upper = coloca tudo em maiúscula
