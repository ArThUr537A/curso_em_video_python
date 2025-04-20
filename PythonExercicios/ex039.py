import datetime
nasc = int(input('Ano de Nascimento: '))
atual = datetime.datetime.now()
idade = atual.year - nasc
if atual.year - nasc == 18:
    print('Quem nasceu em {} tem {} anos em {}.\nVocê tem que se alistar \33[31mIMEDIATAMENTE!.'.format(nasc, idade, atual.year))
elif atual.year - nasc   < 18:
    print('Quem nasceu em {} tem {} anos em {}.\n\33[32mAinda faltam {} anos para o seu alistamento.\33[m\nSeu alistamento será em {}.'.format(nasc, idade, atual.year,-(atual.year - nasc) + 18, nasc + 18))
elif atual.year - nasc > 18:
    print('Quem nasceu em {} tem {} anos em {}.\n\33[31mVocê já deveria ter se alistado há {} anos.\33[m\nSeu alistamento foi em {}. '.format(nasc,idade,atual.year,(atual.year -nasc) - 18, nasc + 18))
