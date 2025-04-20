'''co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
h = (co**2 + ca**2)**(1/2)
print('O valor da hipotenusa é {:.2f}'.format(h))'''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('O valor da hipotenusa é {:.2f}'. format(hypot(co, ca)))