'''Minha Resolução: '''
# from datetime import datetime
#
# def voto(year):
#     idade = datetime.now().year - y
#     if 16 <= idade < 18 or idade >= 70:
#         print(f'Com {idade} anos o voto é OPCIONAL')
#     elif 18 <= idade < 70:
#         print(f'Com {idade} anos o voto é OBRIGATÓRIO')
#     else:
#         print(f'Com {idade} anos: NÃO VOTA')
#
#
# y = int(input('Em que ano você nasceu? '))
# voto(y)
'''----------------------------------------------------------------------'''
'''Resolução do vídeo: '''
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))
