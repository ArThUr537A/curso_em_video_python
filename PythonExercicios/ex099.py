"""Minha Resolução"""
# from time import sleep
#
# def func(* num):
#     if num == ():
#         print('-=' * 30)
#         print('Analisando os valores passados...')
#         print('Foram informados 0 valores ao todo.')
#         print('O maior valor informado foi 0.')
#     else:
#         print('-='*30)
#         print('Analisando os valores passados...')
#         sleep(0.5)
#         for c in range(0, len(num)):
#             print(f'{num[c]} ', end='')
#             sleep(0.5)
#         print(f'Foram informados {len(num)} valores ao todo')
#         print(f'O maior valor foi {max(num)}')
#
#
# func(2, 9, 4, 5, 7, 1)
# func(4, 7, 0)
# func(6)
# func()
'''-------------------------------------------------------------------------------'''
'''Solução do vídeo: '''
# from time import sleep
#
# def maior(* núm):
#     cont = maior = 0
#     print('-=' * 30)
#     print('Analisando os valores passados...')
#     for valor in núm:
#         print(f'{valor} ', end='')
#         sleep(0.3)
#         if cont == 0:
#             maior = valor
#         else:
#             if valor > maior:
#                 maior = valor
#         cont += 1
#     print(f'Foram informados {cont} valores ao todo.')
#     print(f'O maior valor informado foi {maior}.')
#
# maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 0)
# maior(1, 2)
# maior(6)
# maior()
