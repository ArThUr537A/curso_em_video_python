s1= float(input('O primeiro segmento: '))
s2 = float(input('O segundo segmento: '))
s3 = float(input('O terceiro segmento: '))
if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    if s1 == s2 == s3:
        print('Os segmentos formam um triângulo equilátero.')
    elif s1 == s2 != s3 or s1 == s3 != s2:
        print('Os segmentos formam um triângulo isósceles.')
    else:
        print('Os segmentos formam um triângulo escaleno.')
else:
    print('Os segmentos computados não formam um triângulo.')