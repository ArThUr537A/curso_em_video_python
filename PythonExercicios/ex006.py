n1 = int(input('\033[4;34mDigite um número:\033[m '))
cores = {'limpa':'\033[m', 'vermelho':'\033[31m', 'roxo':'\033[35m', 'ciano':'\033[36m'}
print('O dobro de {} vale {}{}{}'.format(n1, cores['vermelho'], n1*2, cores['limpa']))
print('O triplo de {} vale {}{}{}'.format(n1, cores['roxo'], n1*3, cores['limpa']))
print('A ráiz quadrada de {} vale {}{:.2}{}'.format(n1, cores['ciano'], n1**(1/2), cores['limpa']))
