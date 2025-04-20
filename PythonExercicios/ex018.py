from math import sin, cos, tan, pi
a = float(input('Digite o ângulo desejado: '))
seno = sin(a*(pi/180))
cos = cos(a*(pi/180))
tang = tan(a*(pi/180))
print('O SENO de {} é {:.2f}.'.format(a, seno))
print('O COSSENO de {} é {:.2f}.'.format(a, cos))
print('A TANGENTE de {} é {:.2f}.'.format(a, tang))