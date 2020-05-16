from math import sqrt,pow

c1 = float(input('Digite o cateto 1: '))
c2 = float(input('Digite o cateto 2: '))

h = sqrt(pow(c1,2)+pow(c2,2))

print('A hipotenusa mede: {}cm'.format(h))