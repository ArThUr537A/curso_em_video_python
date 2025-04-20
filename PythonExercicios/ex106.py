'''Minha Resolução: '''
# from time import sleep
# def intHelp():
#     while True:
#         print('\033[1;30;42m~'*25)
#         print('SISTEMA DE AJUDA PyHELP')
#         print('~'*25)
#         print('\033[m')
#         fun_bibl = input('Função ou Biblioteca > ')
#         if fun_bibl == 'fim':
#             print('\033[1;30;41m~' * 10)
#             print('ATÉ LOGO!')
#             print('~' * 10)
#             break
#         else:
#             print('\033[0;30;44m~' * 35)
#             print(f"Acessando o manual de comando '{fun_bibl}'")
#             print('~' * 35)
#             print('\033[m')
#             sleep(2)
#             manual = str(help(fun_bibl))
#             print(f'{manual}')
#
# intHelp()
'-----------------------------------------------------------------------------'
'''Resolução do vídeo: '''
from time import sleep
c= ('\033[m',        # 0 - sem cores
    '\033[0;30;41m', # 1  - vermelho
    '\033[0;30;42m', # 2  - verde
    '\033[0;30;43m', # 3  - amarelo
    '\033[0;30;44m', # 4  - azul
    '\033[0;30;45m', # 5  - roxo
    '\033[7;30m',    # 6  - branco
   )

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[5], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)
#Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)
