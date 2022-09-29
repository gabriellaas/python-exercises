# embaralhar sequência em uma lista
from random import shuffle

stud1 = input('Digite o primeiro aluno: ')
stud2 = input('Digite o segundo aluno: ')
stud3 = input('Digite o terceiro aluno: ')
stud4 = input('Digite o quarto aluno: ')
lista = [stud1, stud2, stud3, stud4]
shuffle(lista)
print('A sequência é: {}.'.format(lista))
