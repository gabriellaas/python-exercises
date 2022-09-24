wage = float(input('Digite o seu salário: '))
increase = wage + (wage * 0.15)
print('O novo salário é R${:.2f}.'.format(increase))

# resumido:
wage = float(input('Digite o seu salário: '))
print('O novo salário é R${:.2f}.'.format(wage + (wage * 0.15)))

# especificando a % de aumento:
wage = float(input('Digite o seu salário: '))
percent = int(input('Digite a % de aumento: '))
increase = wage + (wage * (percent/100))
print('O novo salário é R${:.2f}.'.format(increase))
