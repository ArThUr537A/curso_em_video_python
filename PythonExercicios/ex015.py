d = int(input('Quantidade de dias alugados:'))
km = float(input('Quantidade de km rodados:'))
pagar = (d * 60) + (km * 0.15)
print('Total a pagar R${:.2f}.'.format(pagar))