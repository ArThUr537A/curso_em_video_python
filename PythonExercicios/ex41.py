import datetime
atual = datetime.datetime.now().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
if idade <= 9:
    print('Atleta tem {} anos.\nClassificação: MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Atleta tem {} anos.\nClassificação: INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Atleta tem {} anos.\nClassificação: JUNIOR'.format(idade))
elif idade > 19 and idade <= 25:
    print('Atleta tem {} anos.\nClassificação: SÊNIOR'.format(idade))
else:
    print('Atleta tem {} anos.\nClassficação: MASTER'.format(idade))