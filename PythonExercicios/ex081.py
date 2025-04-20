'''Minha solução'''
# valores = []
# pergunta = 'S'
# while 'S' in pergunta:
#     valor = int(input('Digite um valor: '))
#     pergunta = input('Quer continuar: [S/N]').upper()
#     valores.append(valor)
# print('-=' * 30)
# print(f'Você digitou {len(valores)} elementos')
# print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')
# if 5 in valores:
#     print('O valor 5 faz parte da lista')
# else:
#     print('O valor 5 não foi encontrado na lista')
'''-------------------------------------------------------------------------------------'''
'''Solução do vídeo'''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
