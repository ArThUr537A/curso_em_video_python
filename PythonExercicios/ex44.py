print('========== LOJAS GUANABARA ==========')
valor = float(input('Qual o valor do produto em R$: '))
print('Qual a forma de pagamento?')
tabela = int(input('[1] à vista dinheiro/cheque\n[2] à vista cartão\n[3] em até 2x no cartão\n[4] 3x ou mais no cartão\nSua opção:'))
if tabela == 1:
    desconto = (valor - valor*0.10)
    print('O valor a vista ganha 10% de desconto. Você deve pagar R${}'.format(desconto))
elif tabela == 2:
    desconto = (valor - valor*0.05)
    print('O valor a vista no cartão ganha 5% de desconto. Você deve pagar R${}'.format(desconto))
elif tabela == 3:
    print('O valor em até 2x no cartão não recebe juros. Você deve pagar R${}'.format(valor))
elif tabela == 4:
    juros = (valor + (valor * 0.2))
    print('O valor em até 3x ou mais no cartão recebe 20% de juros. Você deve pagar R${}'.format(juros))
else:
    print('Valor INVÁLIDO!')