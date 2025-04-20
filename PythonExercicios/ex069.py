conti = masc = femin = 0
while True:
    print('='*20)
    print('CADASTRE UMA PESSOA')
    print('='*20)
    idade = int(input('Idade: '))
    sexo = ' '
    continuar = ' '
    while sexo not in 'MF':
        while sexo not in 'MF':
            sexo = input('Sexo: [M/F] ').strip().upper()[0]
    if idade > 18:
        conti += 1
    if sexo == 'M':
        masc += 1
    print('='*20)
    if sexo == 'F' and idade < 20:
        femin += 1
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {conti}')
print(f'Ao todo temos {masc} homens cadastrados')
print(f'E temos {femin} mulheres com menos de 20 anos')
