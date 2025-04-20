'''Minha solução'''
# lista = []
# while True:
#     valor = int(input('Digite um valor: '))
#     if valor in lista:
#         print('Valor duplicado! Não vou adicionar...')
#     else:
#         lista.append(valor)
#         confirma = str(input('Quer continuar? [S/N]'))
#         while confirma not in 'SNsn':
#             print('Valor inválido! Tente novamente.')
#             confirma = str(input('Quer continuar? [S/N]'))
#         if confirma in 'Nn':
#             break
# print(f'Você digitou os valores {sorted(lista)}')
'''Parece funcionar perfeitamente e ainda válida se a pessoa digitou certo o sim ou não.'''

'''Solução do vídeo'''
# números = list()
# while True:
#     n = int(input('Digite um valor: '))
#     if n not in números:
#         números.append(n)
#         print('Valor adicionado com sucesso...')
#     else:
#         print('Valor duplicado! Não vou adicionar')
#     r = str(input('Quer continuar? [S/N]'))
#     if r in 'Nn':
#         break
# print('-=' * 30)
# números.sort()
# print(f'Você digitou os valores {números}')