print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(1,11):
    print(p + (c-1)*r, end='-> ')
print('ACABOU!')

