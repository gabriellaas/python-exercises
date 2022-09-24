n = int(input('Digite um número: '))
print('O dobro de {} é {}, o triplo é {} e a raiz é {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))

# exponenciação (elevado a) = **
# raiz quadrada = **(1/2)

# utilizando a função power:
# pow(base, expoente)
n = int(input('Digite um número: '))
print('O dobro de {} é {}, o triplo é {} e a raiz é {:.2f}.'.format(n, (n*2), (n*3), pow(n, 1/2)))
