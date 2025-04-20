from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
n = randint(0, 5)
m = int(input('Em que número eu pensei?  '))
print('PROCESSANDO...')
sleep(2)
if m == n:
    print('O número que eu pensei foi {}. Parabens! você acertou!'.format(n))
else:
    print('O número que eu pensei foi {}. Lamento! você errou!'.format(n))
