# Minha solução:
'''print('-_-'*20)
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = float(input('Digite outro valor: '))
print('-_-'*20)
if n1>n2 and n1>n3:
    print('O maior valor é {}'.format(n1))
    if n3>n2:
        print('O menor valor é {}'.format(n2))
    if n2>n3:
        print('o menor valor é {}'.format(n3))
if n2>n1 and n2>n3:
    print('O maior valor é {}'.format(n2))
    if n1>n3:
        print('O menor valor é {}'.format(n3))
    if n3>n1:
        print('O menor valor é {}'.format(n1))
if n3>n1 and n3>n2:
    print('O maior valor é {}'.format(n3))
    if n1>n3:
        print('O menor valor é {}'.format(n3))
    if n3>n1:
        print('O menor valor é {}'.format(n1))#'''

# Solução do vídeo:
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é o menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

