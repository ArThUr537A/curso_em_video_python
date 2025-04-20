"""Minha Resolução: """
# from time import sleep
#
# def contxyz(x, y, z):
#     print('=-' * 20)
#     if x > y and z > 0:
#         print(f'Contagem de {x} até {y} de {z} em {z}')
#         for c in range(x, y - 1, (-1) * z):
#             print(f'{c} ', end='')
#             sleep(0.5)
#         print(' FIM!')
#     elif x > y and z < 0:
#         print(f'Contagem de {x} até {y} de {(-1) * z} em {(-1) * z}')
#         for c in range(x, y - 1, z):
#             print(f'{c} ', end='')
#             sleep(0.5)
#         print(' FIM!')
#     elif x < y and z > 0:
#         print(f'Contagem de {x} até {y} de {z} em {z}')
#         for c in range(x, y + 1, z):
#             print(f'{c} ', end='')
#             sleep(0.5)
#         print(' FIM!')
#     elif x < y and z < 0:
#         print(f'Contagem de {x} até {y} de {(-1) * z} em {(-1) * z}')
#         for c in range(x, y + 1, (-1) * z):
#             print(f'{c} ', end='')
#             sleep(0.5)
#         print(' FIM!')
#     print()
#
#
# contxyz(1, 10, 1)
# contxyz(10, -1, -2)
# x = int(input('Inicio: '))
# y = int(input('Fim: '))
# z = int(input('Passo: '))
# contxyz(x, y, z)
'''-----------------------------------------'''
"""Resolução do vídeo: """
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
   
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)