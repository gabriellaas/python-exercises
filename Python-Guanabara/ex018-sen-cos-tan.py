from math import radians, sin, cos, tan

angle = float(input('Digite um ângulo: '))
print('O seno de {} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'
      .format(angle, sin(radians(angle)), cos(radians(angle)), tan(radians(angle))))
