'''Minha solução!'''
# valores = []
# for valor in range(0,5):
#     value = input(f'Digite o valor na posição {valor}: ')
#     valores.append(value)
# print('-='*25)
# print(f'Você digitou os valores: {valores}.')
#
# valores_maximos = valores[:]
# index_valores_maximos = []
#
# for i, valor in enumerate(valores_maximos):
#     if valor < max(valores):
#         valores_maximos[i] = 0
#     else:
#         index_valores_maximos.append(i)
#
# valores_minimos = valores[:]
# index_valores_minimos = []
#
# for i, valor in enumerate(valores_minimos):
#     if valor > min(valores):
#         valores_minimos[i] = 0
#     else:
#         index_valores_minimos.append(i)
# print(index_valores_maximos, index_valores_minimos)
# print(f'O maior valor digitado foi {max(valores)} nas posições {index_valores_maximos[0]}... {index_valores_maximos[1]}...')
'''Minha solução da erro se eu não digitar dois valores máximos e dois valores mínimos.'''

'''Solução do Vídeo'''
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print('\t')
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
'''Solução do vídeo resolve o problema que eu estava tendo na minha solução de forma que eu posso repetir quantos valores
   eu quiser, ele faz isso usando uma estrutura de if para saber se o valor é maior ou menor e usa um laço de repetição
   para escrever os indices dos maiores e menores valores.'''