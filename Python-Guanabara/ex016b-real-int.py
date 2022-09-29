from math import trunc

number = float(input('Digite um número: '))
print('A parte inteira do número {} é {}.'.format(number, trunc(number)))

# sem importar lib:
number = float(input('Digite um número: '))
print('A parte inteira é {}.'.format(int(number)))
