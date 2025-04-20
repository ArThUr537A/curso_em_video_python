casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual é o seu salario? R$ '))
anos = int(input('Em quantos anos você vai pagar? '))
prestação = casa/(12*anos)
print('Para pagar uma casa de R${} em {} anos a prestação será R${:.2f}'.format(casa, anos, prestação))
if prestação <= salario * 0.3:
    print('Emprestimo \033[32mCONCEDIDO!\033[m')
else:
    print('Emprestimo \033[31mNEGADO!\033[m')