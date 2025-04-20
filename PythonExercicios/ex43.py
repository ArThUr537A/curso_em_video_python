massa = float(input('Qual a massa a sua massa (Kg): '))
altura = float(input('Qual a sua altura (m): '))
imc = massa/(altura**2)
if imc <= 18.5:
    print('Seu IMC é {:.2f}. Você está ABAIXO DO PESO!'.format(imc))
elif imc <= 25:
    print('Seu IMC é {:.2f}. Você está NORMAL!'.format(imc))
elif imc <= 30:
    print('Seu IMC é {:.2f}. Você está SOBREPESO!'.format(imc))
elif imc <= 40:
    print('Seu IMC é {:.2f}. Você está em OBESIDADE!'.format(imc))
else:
    print('Seu IMC é {:.2f}. Você está em OBESIDADE MORBIDA!'.format(imc))
