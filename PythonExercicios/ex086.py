'''Minha solução'''
# matriz = [[], [], []]
# for c in range(0, 9):
#     if c <= 2:
#         matriz[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
#     elif c > 2 and c <= 5:
#         matriz[1].append(int(input(f'Digite um valor para [1, {c-3}]: ')))
#     else:
#         matriz[2].append(int(input(f'Digite um valor para [2, {c-6}]: ')))
# print('-=' * 30)
# print(f'[ {matriz[0][0]} ]' + f'[ {matriz[0][1]} ]' + f'[ {matriz[0][2]} ]')
# print(f'[ {matriz[1][0]} ]' + f'[ {matriz[1][1]} ]' + f'[ {matriz[1][2]} ]')
# print(f'[ {matriz[2][0]} ]' + f'[ {matriz[2][1]} ]' + f'[ {matriz[2][2]} ]')
'''---------------------------------------------------------------------------'''
'''Solução do vídeo'''
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# print('-=' * 30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()