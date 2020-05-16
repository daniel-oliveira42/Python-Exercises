pt = int(input('Escreva o primeiro termo da PA: '))
raz = int(input('Escreva a razão da PA: '))
c=0
mais = 10
lim = 0
totalt = 10
while mais != 0:
    lim = lim + mais
    while c < lim:
        print('{}, '.format(pt, pt+raz), end='')
        pt += raz
        c+=1
    print(pt)
    mais = int(input('Quantos termos a mais? '))
    totalt += mais
print('A PA teve um total de {} termos'.format(totalt))
      