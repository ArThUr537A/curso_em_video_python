from random import randint
numeros_sorteados = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print(f'Os valores sorteados foram: {numeros_sorteados}')
print(f'O maior valor sorteado foi: {max(numeros_sorteados)}')
print(f'O menor valor sorteado foi: {min(numeros_sorteados)}')