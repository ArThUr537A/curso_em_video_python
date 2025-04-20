# Minha Resolução:

'''from time import sleep

primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
escolha = 0
while escolha != 5:
    escolha = int(input(
        '[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n>>>>> Qual a sua opção? '))
    if escolha == 1:
        soma = primeiro + segundo
        print('A soma dos entre {} e {} é {}.'.format(primeiro, segundo, soma))
        print('=-' * 20)
        sleep(2)
    elif escolha == 2:
        produto = primeiro * segundo
        print('O produto entre {} e {} é {}.'.format(primeiro, segundo, produto))
        print('=-' * 20)
        sleep(2)
    elif escolha == 3:
        lista = [primeiro, segundo]
        print('Entre {} e {} o maior é {}.'.format(primeiro, segundo, max(lista)))
        print('=-' * 20)
        sleep(2)
    elif escolha == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo vaor: '))
        print('=-' * 20)
        sleep(2)
    elif escolha == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Valor inválido. Tente novamente.')'''

# Resolução do vídeo:
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de  {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    sleep(2)
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')
