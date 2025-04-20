'''Minha Resolução:'''
# jogador = dict()
# partidas = list()
# time = list()
# while True:
#     partidas.clear()
#     jogador['nome'] = str(input('Nome do Jogador: '))
#     tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
#     for c in range(0, tot):
#         partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
#     jogador['gols'] = partidas[:]
#     jogador['total'] = sum(partidas)
#     jogador_n = jogador.copy()
#     cont = str(input('Quer continuar? [S/N]')).upper()[0]
#     time.append(jogador_n)
#     if cont in 'N':
#         break
# print('-=' * 40)
# print(f'{"cod nome"}{"gols".rjust(30)}{"total".rjust(30)}')
# print('--' * 40)
# cont = 0
# for k, v in enumerate(time):
#     print(f'{cont:<} {v["nome"]}{str(v["gols"]).rjust(30)}{str(v["total"]).rjust(30)}')
#     cont += 1
# while True:
#     dados_jogador = int(input('Mostrar dados de qual jogador? (999 para parar)'))
#     if dados_jogador == 999:
#         print('<<<VOLTE SEMPRE>>>')
#         break
#     elif dados_jogador < len(time):
#         print(f'LEVANTAMENTO DO JOGADOR {time[dados_jogador]['nome']}:')
#         for c in range(0, len(time[dados_jogador]['gols'])):
#             print(f'No jogo {c} fez {time[dados_jogador]['gols'][c]}')
#     else:
#         print(f'ERRO! não existe jogador com código {dados_jogador}')
'''-----------------------------------------------------------------------------------------------------'''
'''Resolução do vídeo:'''
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código de busca {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< Volte Sempre >>')