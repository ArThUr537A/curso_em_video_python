l = float(input('Largura da parede:'))
a = float(input('Alatura da parede:'))
A = l*a
print('Sua parede tem dimensão de {}x{} e sua área é de {}m².\n''Para pintar essa parede, você precisará de {}l de tinta.'.format(l, a, A,A/2 ))