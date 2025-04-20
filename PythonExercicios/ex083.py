'''Minha solução'''
# expressao = str(input('Digite a sua expressão: '))
# lista_expressao = list(expressao)
# cont = 0
# for caracter in lista_expressao:
#     if caracter in '()':
#         cont += 1
# if cont % 2 == 0:
#     print('Sua expressão está válida!')
# else:
#     print('Sua expressão não está válida!')
'''----------------------------------------------------'''
'''Solução do vídeo!'''
# expr = str(input('Digite a expressão: '))
# pilha = []
# for símb in expr:
#     if símb == '(':
#         pilha.append('(')
#     elif símb == ')':
#         if len(pilha) > 0:
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break
# if len(pilha) == 0:
#     print('Sua expressão está válida!')
# else:
#     print('Sua expressão está errada!')