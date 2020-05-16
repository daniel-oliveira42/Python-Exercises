a = int(input('Insira o valor A: '))
b = int(input('Insira o valor B: '))
c = int(input('Insira o valor C: '))

if a > c and a > b:
    maior = a
    if b > c:
        menor = c
    else:
        menor = b
elif b > c and b > a:
    maior = b
    if a > c:
        menor = c
    else:
        menor = a
elif c > a and c > b:
    maior = c
    if b > a:
        menor = a
    else:
        menor = b

print('O maior valor é: ', maior)
print('O menor valor é: ', menor)
