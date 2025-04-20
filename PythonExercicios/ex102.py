'''Minha Resolução: '''
# def fatorial(n, show=True):
#     """
#     -> Calcula o Fatorial de um número.
#     :param n: O número a ser calculado
#     :param show: (opcional) Mostra ou não a conta
#     :return: O valor do fatorial de um número n.
#     """
#     if show:
#         c = n
#         print('-' * 30)
#         while c != 1:
#             print(f' {c} x', end='')
#             c -= 1
#             n = n * c
#         print(f' {1} = {n}')
#     else:
#         c = n
#         print('-' * 30)
#         while c != 1:
#             c -= 1
#             n = n * c
#         print(f'{n}')
#
#
# fatorial(10, show=True)
# help(fatorial)
'''----------------------------------------------------------------------------'''
'''Resolução do vídeo: '''
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
print(fatorial(5, show=False))
help(fatorial)
