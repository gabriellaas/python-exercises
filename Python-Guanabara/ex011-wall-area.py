height = float(input('Digite a altura: '))
width = float(input('Digite a largura: '))
area = height * width
print('A área da parede é {:.2f}m e a quantidade de litros de tinta necessária é de {:.2f} galões.'
      .format(area, area/2))

# forma resumida:
height = float(input('Digite a altura: '))
width = float(input('Digite a largura: '))
print('A área da parede é {:.2f}m e a quantidade de galões necessária é {:.2f}.'
      .format((height * width), (height * width)/2))

# número inteiro de galões
height = float(input('Digite a altura: '))
width = float(input('Digite a largura: '))
area = height * width
gallons = (area // 2)
total = gallons + (gallons % 2)
print('A área da parede é {:.2f}m e a quantidade de galões necessária é {:.0f}.'
      .format(area, total))
