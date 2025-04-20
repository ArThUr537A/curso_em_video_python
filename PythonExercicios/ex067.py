while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    if tab < 0:
        break
    for c in range(1, 11):
        print(f'{tab} x {c} = {tab*c}')
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
