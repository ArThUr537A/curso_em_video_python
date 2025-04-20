salario = float(input('Qual é o sálario do funcinário? R$ '))
if salario <= 1250.00:
    print('Quem ganhava R${} passa a ganhar R${:.2f}!'.format(salario, (salario * 0.15) + salario))
else:
    print('Quem ganhava R${} passa a ganhar R${:.2f}!'.format(salario, (salario * 0.10) + salario))
