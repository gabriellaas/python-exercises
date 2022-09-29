import random

first = input('Digite o primeiro aluno: ')
second = input('Digite o segundo aluno: ')
third = input('Digite o terceiro aluno: ')
fourth = input('Digite o quarto aluno: ')
lista = [first, second, third, fourth]
print('O aluno escolhido foi: {}.'.format(random.choice(lista)))
