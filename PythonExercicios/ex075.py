n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
numeros = (n1, n2, n3, n4)
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1} posição.')
else:
    print(f'O valor 3 não está na lista!')

print('Os valores pares digitados foram ', end='')
cont = 0
for c in range(0, 4):
    if numeros[c] % 2 == 0:
        print(numeros[c], end=' ')
        cont += 1

if cont == 0:
    print('nenhum!')





