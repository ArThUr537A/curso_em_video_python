n1 = float(input('Uma distância em metros:'))
print('{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm\n'.format(n1/1000, n1/100, n1/10, n1*10, n1*100, n1*1000))