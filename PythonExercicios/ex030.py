numero = int(input('Digite um número inteiro: '))
resto = numero % 2
if numero % 2 == 0:
    print('Esse número {} é PAR!'.format(numero))
else:
    print('Esse número {} é IMPAR!'.format(numero))