def ficha(jog='<Desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

n = str(input('Nome do Jogador: '))
g = str(input('Número de gols: '))
print(type(g))
if g.isnumeric():
     g =int(g)
else:
    g = 0
if n == '':
    ficha(gol=g)
else:
    ficha(n, g)
'''----------------------------------------------------------------------------'''
'''Resolução do Vídeo'''
# def ficha(jog='<Desconhecido>', gol=0):
#     print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')
#
# #Programa principal
# n = str(input("Nome do Jogador: "))
# g = str(input("Número de gols "))
# if g.isnumeric():
#     g = int(g)
# else:
#     g = 0
# if n.strip() == '':
#     ficha(gol=g)
# else:
#     ficha(n, g)