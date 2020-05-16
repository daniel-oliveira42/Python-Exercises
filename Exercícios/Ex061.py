pt = int(input('Escreva o primeiro termo da PA: '))
raz = int(input('Escreva a razão da PA: '))
c=0
while c < 9:
    print('{}, '.format(pt, pt+raz),end='')
    pt += raz
    c += 1
print(pt)
