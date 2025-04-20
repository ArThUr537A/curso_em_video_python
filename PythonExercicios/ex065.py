núm = cont = soma = média = maior = menor = 0
afirm = str('S')
while afirm != str('N'):
    núm = int(input('Digite um número: '))
    afirm = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    cont += 1
    soma += núm
    if cont == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
print('Você digitou {} números e a média foi {}'.format(cont,soma/cont))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
