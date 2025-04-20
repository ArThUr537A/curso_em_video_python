# import time
# import random
# jogadas = dict()
# for c in range(0, 4):
#     num = random.randint(1, 6)
#     print(f'jogador{c+1} tirou {num} no dado.')
#     jogadas[f'jogador{c+1}'] = num
# print(jogadas.items())
# jogadas_ord = dict()
# for c in range(0, 4):
#     jogadas_ord[f'jogador{c+1}'] = 0
# print(jogadas_ord)
'''Não consegui resolver'''
'''--------------------------------------------------------------------'''
'''Solução do vídeo'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)