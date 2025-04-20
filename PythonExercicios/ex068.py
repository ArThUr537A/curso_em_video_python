from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
cont = 0
while True:
    núm = int(input('Diga um valor: '))
    pi = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    print('-'*40)
    com = randint(1,11)
    tot = núm + com
    if tot % 2 == 0:
        print(f'Você jogou {núm} e o computador jogou {com}. Total de {tot} deu par')
        print('-'*40)
        if pi == 'P':
            print('Você VENCEU!')
            cont += 1
            print('Vamos jogar novamente...')
        if pi == 'I':
            print('Você PERDEU!')
            break
    else:
        print(f'Você jogou {núm} e o computador jogou {com}. Total de {tot} deu ímpar')
        print('-' * 40)
        if pi == 'I':
            print('Você VENCEU!')
            cont += 1
            print('Vamos jogar novamente...')
        if pi == 'P':
            print('Você PERDEU!')
            break
print(f'Game Over! você venceu {cont} vezes')
