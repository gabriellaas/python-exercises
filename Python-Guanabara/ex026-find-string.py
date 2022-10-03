phrase = str(input('Digite uma frase: ')).strip().upper()
print('Quantas vezes aparece a letra A? {}'.format(phrase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(phrase.find('A') + 1))
print('A última letra A apareceu na posição {}.'.format(phrase.rfind('A') + 1))

# somar +1 para não contar a partir da posição 0, mas sim da 1
# rfind = encontra a última letra à direita
# upper/lower/capitalize para contar todas as ocorrências da letra, independente de como escrita

