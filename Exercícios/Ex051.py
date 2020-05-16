pt = int(input('Insira o termo inicial da PA: '))
raz = int(input('Insira a razão da PA: '))

for c in range(pt, (pt + 9*raz)+raz, raz):
    print(' ', c, end='')