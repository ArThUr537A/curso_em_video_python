'''Minha Resolução'''
# boletim = {'nome': 'vazio', 'nota': 'vazio'}
# nome = input(str('Nome: '))
# media = float(input(f'Media do {nome}: '))
# boletim ['nome'] = nome
# boletim ['nota'] = media
# print('-=' * 20)
# print(f'Nome é igual a {boletim["nome"]}', end='\n')
# print(f'média é igual a {boletim["nota"]}', end='\n')
# if boletim['nota'] < 5:
#     print('Situação é igual a Reprovado')
# elif 5 <= boletim['nota'] < 6:
#     print('Situação é igual a Recuperação')
# else:
#     print('Situação é igual a Aprovado')
'''---------------------------------------------------------------------'''
'''Solução do vídeo'''
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' -{k} é igual a {v}')