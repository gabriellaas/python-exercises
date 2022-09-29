# cálculo da hipotenusa com módulo a partir dos valores dos catetos
from math import hypot

catoposto = float(input('Digite o cateto oposto: '))
catadj = float(input('Digite o cateto adjacente: '))
print('A hipotenusa é {:.2f}.'.format(hypot(catoposto, catadj)))

# usando a fórmula
catoposto = float(input('Digite o cateto oposto: '))
catadj = float(input('Digite o cateto adjacente: '))
hipot = (catoposto ** 2 + catadj ** 2) ** (1/2)
print('A hipotenusa é {:.2f}.'.format(hipot))
