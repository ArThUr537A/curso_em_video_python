'''Minha Solução'''
# informacao = []
# nomes = []
# pesos = []
# pergunta = 'S'
# while pergunta in 'sS':
#     nome = str(input('Nome: '))
#     peso = float(input('Peso: '))
#     nomes.append(nome)
#     pesos.append(peso)
#     informacao.append([nome, peso])
#     pergunta = str(input('Quer continuar? [S/N]'))
#
# print(f'Ao todo você cadastrou {len(informacao)}')
# print(f'O maior peso foi de {max(pesos)}kg. de', end=' ')
#
# for c in range(0, len(informacao)):
#         if informacao[c][1] == max(pesos):
#             print(informacao[c][0], end=', ')
# print('\t')
# print(f'O menor peso foi de {min(pesos)}kg. de', end=' ')
# for c in range(0, len(informacao)):
#     if informacao[c][1] == min(pesos):
#         print(informacao[c][0], end=', ')
'''----------------------------------------------------------------------------'''
'''Solução do vídeo'''
# temp = []
# princ = []
# mai =men = 0
# while True:
#     temp.append(str(input('Nome: ')))
#     temp.append(float(input('Peso: ')))
#     if len(princ) == 0:
#         mai = men = temp[1]
#     else:
#         if temp[1] > mai:
#             mai = temp[1]
#         if temp[1] < men:
#             men = temp[1]
#     princ.append(temp[:])
#     temp.clear()
#     resp =str(input('Quer continuar? [S/N]'))
#     if resp in 'Nn':
#         break
# print('-=' * 30)
# print(f'Os dados foram {princ}')
# print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
# print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
# for p in princ:
#     if p[1] == mai:
#         print(f'[{p[0]}] ', end= '')
# print()
# print(f'O menor peso foi de {men}Kg. Peso de ', end='')
# for p in princ:
#     if p[1] == men:
#         print(f'[{p[0]}] ', end='')