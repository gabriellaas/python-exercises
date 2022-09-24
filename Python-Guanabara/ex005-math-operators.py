n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
sum = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divint = n1 // n2
expo = n1**n2
print('A soma vale {}, a subtração vale {} e a multiplicação vale {}.'.format(sum, sub, mult))
print('A divisão vale {:.2f}, a divisão inteira vale {} e a exponenciação vale {}.'.format(div, divint, expo))

# formatação na quantidade de caracteres: {:.Xf}, em que X é o número de casas decimais

# quebra de linha = \n
# para forçar que não quebre linha em dois prints seguidos = colocar end='' ao final
# ex.: print('A soma é {}'.format(sum), end='')
