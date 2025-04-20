import datetime
hoje = int(datetime.date.today().year)
cont1 = 0
cont2 = 0
for c in range(1, 8):
    data = int(input('Em que ano a {}° pessoa nasceu?'.format(c)))
    if hoje - 21 < data:
        cont1 += 1
    else:
        cont2 += 1
print('Ao todo tivemos {} maiores de idade\n'
      'E tambem tivemos {} pessoas menores de idade'.format(cont2,cont1))