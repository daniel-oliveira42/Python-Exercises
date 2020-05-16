saque = int(input('Escreva o valor a ser sacado: '))
total = saque
c50 = c20 = c10 = c1 = 0
if total > 50:
    while total >= 50:
        total = total - 50
        c50+=1
    while total >= 20:
        total = total - 20
        c20+=1
    while total >= 10:
        total = total - 10
        c10 += 1
    while total > 0:
        total = total - 1
        c1 += 1
elif total > 20:
    while total >= 20:
        total = total - 20
        c20+=1
    while total >= 10:
        total = total - 10
        c10 += 1
    while total > 0:
        total = total - 10
        c1 += 1
elif total > 10:
    while total >= 10:
        total = total - 10
        c10+=1
    while total > 0:
        total = total - 1
        c10 += 1
else:
    while total > 0:
        total = total - 1
        c1 += 1
print(f'O saque foi de R${saque:.2f}')
print('Tendo um total de: ')
print(f'{c50} notas de 50')
print(f'{c20} notas de 20')
print(f'{c10} notas de 10')
print(f'{c1} moedas de 1')
