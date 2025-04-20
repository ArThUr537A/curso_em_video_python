'''Minha Resolução:'''
# def leiaInt(n):
#     while True:
#         num = str(input('Digite um número: '))
#         if num.isnumeric():
#             return num
#             break
#         else:
#             print('\033[31mErro! Digite um número inteiro válido.\033[m')
#
#
# #Programa Principal
# n = leiaInt('Digite um número: ')
# print(f'Você acabou de digitar o número {n}.')
'''-----------------------------------------------------------------------------------'''
'''Resolução do vídeo:'''
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')