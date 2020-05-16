maior = 0
menor = 0
for c in range(0,7):
    id = int(input('Escreva sua idade em anos: '))
    if id < 21:
        menor += 1
    if id >= 21:
        maior += 1
print('Tem {} de maior'.format(maior))
print('Tem {} de menor'.format(menor))
