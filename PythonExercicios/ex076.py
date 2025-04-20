#Minha solução

'''lista = ('-' * 40,
         ' ' * 12 + 'LISTAGEM DE PREÇOS',
         '-' * 40,
         'Lápis' + '.' * 37 + 'R$  1.75',
         'Borracha' + '.' * 34 + 'R$  2.00',
         'Caderno' + '.' * 35 + 'R$  15.90',
         'Estojo' + '.' * 36 + 'R$  25.00',
         'Transferidor' + '.' * 30 + 'R$  4.20',
         'Compasso' + '.' * 34 + 'R$  9.99',
         'Mochila' + '.' * 35 + 'R$  120.32',
         'Canetas' + '.' * 35 + 'R$  22.30',
         'Livro' + '.' * 37 + 'R$  34.90',
         '')
for c in range (0, len(lista)):
    print(lista[c])'''

#Solução do vídeo

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)