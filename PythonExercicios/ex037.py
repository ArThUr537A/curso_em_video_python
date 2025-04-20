num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão')
print('[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] coverter para HEXADECIMAL\n')
con = int(input('Sua opção: '))
if con == 1:
    print(format(num, "b"))
elif con == 2:
    print(format(num, "o"))
elif con == 3:
    print(format(num, "x"))
else:
    print('\033[31mOPÇÃO INVÁLIDA!')
