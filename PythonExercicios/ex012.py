preço = float(input('Qual o preço do porduto? R$'))
desconto = preço * 0.05
final = preço - desconto
print('O produto que custava R${:.2f}, na promoção com 5% vai custar R${:.2f}.'.format(preço, final))