#Minha resolução
'''print('Gerador de PA')
print('-=' * 10)
Primeiro = int(input('Primeiro termo: '))
Razao = int(input('Razão da PA: '))
contador = 0
while contador <= 9:
    contador += 1
    print(Primeiro + (contador - 1)*Razao, end=' -> ')
print('Fim!')'''

#Resolução do Vídeo:
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA:  '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end=' ')
    termo += razão
    cont += 1
print('Fim!')

