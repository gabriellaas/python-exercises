amount = float(input('Digite o valor que você tem em reais: '))
print('O valor R${:.2f} equivale a US${:.2f}.'.format(amount, (amount / 3.27)))

# outra opção:
amount = float(input('Digite o valor que você tem: '))
dollar = float(input('Digite o valor do dólar hoje: '))
print('O valor R${:.2f} equivale a US${:.2f}.'.format(amount, (amount / dollar)))
