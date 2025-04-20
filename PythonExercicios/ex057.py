# Minha resolução:

"""sexo = str('')
while sexo != 'M' and sexo != 'F':
    sexo = input('Qual é seu sexo:[M/F] ').strip().upper()
    while sexo != 'M' and sexo != 'F':
        if sexo != 'M' and sexo != 'F':
            sexo = input('Dados inválidos. por favor, informe seu sexo: ').strip().upper()
print('Sexo {} registrado com sucesso.'.format(sexo))"""

# Resolução do Vídeo:

"""sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))"""
