'''Minha resolução:'''
# def area(a, b):
#     print(f'A área de um terrreno {a}x{b} é de {a*b}')
#
# print('Controle de terrenos:')
# print('-'*21)
# l = float(input('LARGURA (m): '))
# c = float(input('COMPRIMENTO (m): '))
# area(l, c)
'''Resolução do vídeo: '''
def área(larg, comp):
    a = larg*comp
    print(f'A área de um terrreno {larg}x{comp} é de {a}m²')


print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
