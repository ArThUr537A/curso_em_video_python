'''Minha Resolução'''
# dados = {}
# dados['nome'] = str(input('Nome: '))
# dados['nasc'] = int(input('Ano de Nascimento: '))
# dados['cart'] = int(input('Carteira de Trabalho (0 não tem): '))
# if dados['cart'] != 0:
#     dados['contr'] = int(input('Ano de contratação: '))
#     dados['sal'] = float(input('Salário: R$'))
#     print(f'-nome tem o valor {dados["nome"]}')
#     print(f'-idade tem o valor {2023 - dados["nasc"]}')
#     print(f'-ctps tem o valor {dados["cart"]}')
#     print(f'-contratação tem o valor {dados["contr"]}')
#     print(f'-salário tem o valor {dados["sal"]}')
#     print(f'-aposentatoria tem o valor {2023 -dados["nasc"] + 30}')
# else:
#     print(f'-Nome tem o valor {dados["nome"]}')
#     print(f'-idade tem o valor {2023 - dados["nasc"]}')
#     print(f'-ctps tem o valor {dados["cart"]}')
'''------------------------------------------------------------------------'''
'''Resoulção do vídeo'''
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados ['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f' -{k} tem o valor {v}')