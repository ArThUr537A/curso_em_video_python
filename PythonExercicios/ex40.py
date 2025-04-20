n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda Nota: '))
m = (n1+n2)/2
if m >= 7:
    print('Média igual a {} você está \033[32mAPROVADO!'.format(m))
elif m >= 5 and m < 6.9:
    print('Média igual a {} você está de \033[33mRECUPERAÇÃO!'.format(m))
else:
    print('Média igual a {} você está \033[31mREPROVADO!'.format(m))