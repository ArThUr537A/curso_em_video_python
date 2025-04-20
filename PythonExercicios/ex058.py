# Minha Resolução
from random import randint
n = randint(0, 10)
print('Acabei de pensar em um número de 0 a 10.\n'
      'Será que vc consegue adivinhar qual foi?')
p = 11
cont = 0
while n != p:
    p = int(input('Qual é seu palpite? '))
    cont += 1
    if n > p:
        print('Mais... Tente mais uma vez. ')
    if n < p:
        print('Menos... Tente mais uma vez. ')
print('Acertou com {} tentativas. Parabéns!'.format(cont))

# Resolução do Vídeo
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
