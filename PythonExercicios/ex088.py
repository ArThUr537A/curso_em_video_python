'''Minha solução:'''
# from random import randint
# print('-' * 18)
# print('JOGA NA MEGA SENA')
# print('-' * 18)
#
# qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
# print('SORTEANDO 10 JOGOS')
# lista = []
# for c in range(0, qtd_jogos):
#     lista.append([randint(0, 100), randint(0, 100), randint(0, 100),
#                   randint(0, 100), randint(0, 100), randint(0, 100)])
#     for item in lista[c]:
#         while
'''----------------------------------------------------------------------'''
'''Não consegui fazer:('''
'''Solução do vídeo:'''
# from random import randint
# from time import sleep
# lista = list()
# jogos = list()
# print('-' * 30)
# print('      JOGA NA MEGA SENA      ')
# print('-' * 30)
# quant = int(input('Quantos jogos você quer que eu sorteie? '))
# tot = 1
# while tot <= quant:
#     cont = 0
#     while True:
#         num = randint(1, 60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     tot += 1
# print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
# for i, l in enumerate(jogos):
#     print(f'Jogo {i + 1}: {l}')
#     sleep(1)
# print('-=' * 5, '< BOA SORTE! >', '-=' * 5)