SomI = 0
MV = 0
cont = 0
FV = 0
for leitor in range(1,5):
    print('{} {}ª PESSOA {}'.format('-'*3, leitor, '-'*3))
    Nome = str(input('Nome: '.format(leitor)))
    Idade = int(input('Idade: '))
    Sexo = str(input('Sexo [M/F]: '))
    if leitor == 1:
        SomI = Idade
        MV = Idade
    else:
        if Idade > MV and Sexo == 'M':
            homem = Nome
            MV = Idade
        elif Sexo == 'F' and Idade < 20:
            cont = cont + 1

        SomI = SomI + Idade
print('A média de idade do grupo é de {} anos.'.format(SomI/leitor))
print('O homem mais velho tem {} anos e se chama {}.'.format(MV, homem))
print('Ao todo são {} mulher/s com menos de 20 anos.'.format(cont))
