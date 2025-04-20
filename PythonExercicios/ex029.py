velocidade = float(input('Qual a velocidade do seu carro em km/h? '))
if velocidade >80:
    print('Você estava a {}km/h e excedeu o limite de 80km/h, pague uma multa de R${:.2f}.'.format(velocidade, (velocidade-80)*7))
print('Dirija com segurança, e tenha uma boa viajem!')