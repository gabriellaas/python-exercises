m = float(input('Digite o valor em metros: '))
cm = m*100
mm = m*1000
print('O valor {}m em cm é {:.0f}cm e em mm é {:.0f}mm.'.format(m, cm, mm))

# opção resumida:
m = float(input('Digite o valor em metros: '))
print('O valor {}m, em cm é {:.0f}cm e em mm é {:.0f}mm.'.format(m, (m*100), (m*1000)))

# tabela completa:
m = float(input('Digite o valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('O valor {}m convertido é: {:.2f}km, {:.2f}hm, {:.2f}dam, {:.2f}dm, {:.2f}cm, {:.2f}mm.'
      .format(m, km, hm, dam, dm, cm, mm))

# tabela resumida:
m = float(input('Digite o valor em metros: '))
print('O valor {}m convertido é {:.2f}km, {:.2f}hm, {:.2f}dam, {:.2f}dm, {:.2f}cm, {:.2f}mm.'
      .format(m, (m/1000), (m/100), (m/10), (m*10), (m*100), (m*1000)))
