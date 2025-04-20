lista = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
         'Athletico PR', 'Atlético-MG', 'Chapecoense', 'São Paulo', 'América-MG',
         'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba', 'Cuiabá-MT',
         'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print('=-'*15)
print(f'Lista dos times do Brasileirão: {lista}')
print('=-'*15)
print(f'Os 5 primeiros são: {lista[0:5]}')
print('=-'*15)
print(f'Os 4 ultimos são: {lista[-4:]}')
print('=-'*15)
print(f'Times em ordem alfabética: {sorted(lista)}')
print('=-'*15)
if 'Chapecoense' in lista:
        posicao_chapecoense = lista.index('Chapecoense')
        print(f'O Chapecoense está na posição {posicao_chapecoense + 1}ª lista')
else:
    print('O Chapecoense não está na lista')