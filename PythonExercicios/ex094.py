'''Minha Resolução'''
# num_cad = 0
# soma_idade = 0
# pessoas = dict()
# pessoa_lista = list()
# while True:
#     pessoa = pessoa_lista[:]
#     pessoa.append(str(input('Nome: ')))
#     pessoa.append(str(input('Sexo: [M/F] ')))
#     while pessoa[1] not in 'MmFf':
#         print('ERRO! Por favor, digite apenas M ou F.')
#         pessoa[1] = str(input('Sexo: [M/F]'))
#     pessoa.append(int(input('Idade: ')))
#     cont = str(input('Quer Continuar? [S/N] ')).upper()
#     while cont not in 'SsNn':
#         print('ERRO! Responda apenas S ou N.')
#         cont = str(input('Quer Continuar? [S/N] ')).upper()
#     num_cad += 1
#     soma_idade += pessoa[2]
#     pessoas[f'pessoa{num_cad}'] = pessoa
#     if cont in 'Nn':
#         break
# print('-='* 30)
# print(f'A) Ao todo temos {num_cad} pessoas cadastradas.')
# print(f'B) A média de idade é de {soma_idade/len(pessoas)}')
# print(f'C) As mulheres cadastradas foram', end=': ')
# for k, v in pessoas.items():
#     if v[1] in 'Ff':
#         print(v[0], end=', ')
# print(f'\nD) Lista das pessoas que estão acima da média: ')
# for k, v in pessoas.items():
#     if v[2] > soma_idade/len(pessoas):
#         print(f'\tnome = {v[0]}; sexo = {v[1]}; idade = {v[2]}')
'''--------------------------------------------------------------------------------------------------------------------'''
'''Resolução do Vídeo'''
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')