#Minha Resolução:
'''print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)
termos = int(input('Quantos termos você quer mostrar? '))
cont = 0
n1 = 0
n2 = 1
soma = 0
while cont != termos:
    if cont == 0:
        print(0)
    if cont == 1:
        print(1)
    soma = n1 + n2
    print(soma)
    n1 = n2
    n2 = soma
    cont +=1'''
#Resolução do Vídeo:
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~')
print('{} --> {}'.format(t1,t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' --> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' --> Fim!')
