'''Minha Solução'''
# boletim = [[], [], []]
# pergunta = 'sS'
# while pergunta in 'sS':
#     boletim[0].append(str(input('Nome: ')))
#     boletim[1].append(float(input('Nota 1: ')))
#     boletim[2].append(float(input('Nota 2: ')))
#     pergunta = str(input('Quer continuar? [S/N]'))
# print('-=' * 30)
# print('{0:<8}{1:^8}{2:>8}'.format('N°', 'NOME', "MÉDIA"))
# print('-'* 30)
# for c in range(0, len(boletim[0])):
#     print('{0:<8}{1:^8}{2:>8}'.format(c, boletim[0][c], (boletim[1][c]+ boletim[2][c])/2))
# while True:
#     aluno_notas = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
#     if aluno_notas == 999:
#         break
#     else:
#         print(f'Notas de {boletim[0][aluno_notas]} são [{boletim[1][aluno_notas]}, {boletim[2][aluno_notas]}]')
# print('FINALIZANDO...')
# print('<<<< {0:^} >>>>'.format('VOLTE SEMPRE'))
'''---------------------------------------------------------------------------------------------------------------------'''
'''Solução do vídeo: '''
# ficha = list()
# while True:
#     nome = str(input('Nome: '))
#     nota1 = float(input('Nota 1: '))
#     nota2 = float(input('Nota 2: '))
#     media = (nota1 + nota2) / 2
#     ficha.append([nome, [nota1, nota2], media])
#     resp = str(input('Quer continuar? [S/N]'))
#     if resp in 'nN':
#         break
# print('-=' * 30)
# print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
# print('-' * 26)
# for i, a in enumerate(ficha):
#     print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
# while True:
#     print('-' * 35)
#     opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#     if opc == 999:
#         print('FINALIZANDO...')
#         break
#     if opc <= len(ficha) - 1:
#         print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
# print('<<< VOLTE SEMPRE >>>')