n1 = int(input('Digite um número:'))
cores = {'limpa':'\033[m',
        'vermelho':'\033[31m',
         'verde':'\033[32m'}
print('Analisando o valor {}, seu antecessor é {}{}{} e o sucessor é {}{}{}'.format(n1, cores['vermelho'], (n1-1), cores['limpa'], cores['verde'], (n1+1), cores['limpa'] ))
