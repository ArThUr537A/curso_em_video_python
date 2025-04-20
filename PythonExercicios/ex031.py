from time import sleep
distancia = float(input('Digite a distância da viajem em km: '))
print('CALCULANDO O VALOR DA SUA VIAJEM...')
sleep(3)
if distancia <= 200:
    print('O preço da sua passagem é R${}'.format(0.50 * distancia))
else:
    print('O preço da sua passagem é R${}'.format(0.45 * distancia))