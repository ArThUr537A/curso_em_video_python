from random import randint
from time import sleep
print('Suas opções: \n[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ] TESOURA')
n = int(input('Qual a sua jogada? '))
m = randint(1,3)
sleep(1)
print('JO')
sleep(1)
print('KÊN')
sleep(1)
print('PÔ')
print(20 * '-=')
if n == m:
    if n == 1:
        n = 'PEDRA'
        m = 'PEDRA'
        print('Computador jogou {}'.format(m))
        print('Jogador jogou {}'.format(n))
        print(20 * '-=')
        print('EMPATE!')
    elif n == 2:
        n = 'PAPEL'
        m = 'PAPEL'
        print('Computador jogou {}'.format(m))
        print('Jogador jogou {}'.format(n))
        print(20 * '-=')
        print('EMPATE!')
    elif n == 3:
        n = 'TESOURA'
        m = 'TESOURA'
        print('Computador jogou {}'.format(m))
        print('Jogador jogou {}'.format(n))
        print(20 * '-=')
        print('EMPATE!')
elif n == 1 and m == 2:
    n = 'PEDRA'
    m = 'PAPEL'
    print('Computador jogou {}'.format(m))
    print('Jogador jogou {}'.format(n))
    print(20 * '-=')
    print('O COMPUTADOR GANHOU!')
elif n == 1 and m == 3:
    n = 'PEDRA'
    m = 'TESOURA'
    print('Computador jogou {}'.format(m))
    print('Jogador jogou {}'.format(n))
    print(20 * '-=')
    print('O JOGADOR GANHOU!')
elif n == 2 and m == 1:
    n = 'PAPEL'
    m = 'PEDRA'
    print('Computador jogou {}'.format(m))
    print('Jogador jogou {}'.format(n))
    print(20 * '-=')
    print('O JOGADOR GANHOU!')
elif n == 2 and m == 3:
    n = 'PAPEL'
    m = 'TESOURA'
    print('Computador jogou {}'.format(m))
    print('Jogador jogou {}'.format(n))
    print(20 * '-=')
    print('O COMPUTADOR GANHOU!')
elif n == 3 and m == 1:
    n = 'TESOURA'
    m = 'PEDRA'
    print('Computador jogou {}'.format(m))
    print('Jogador jogou {}'.format(n))
    print(20 * '-=')
    print('O COMPUTADOR GANHOU!')
elif n == 3 and m == 2:
    n = 'TESOURA'
    m = 'PAPEL'
    print('Computador jogou {}'.format(m))
    print('Jogador jogou {}'.format(n))
    print(20 * '-=')
    print('O JOGADOR GANHOU!')
else:
    print('JOGADA INVÁLIDA!')
