numeros = (int(input('Escreva o número 1: ')),
           int(input('Escreva o número 2: ')),
           int(input('Escreva o número 3: ')),
           int(input('Escreva o número 4: ')))
print('O valor 9 apareceu {} vezes'.format(numeros.count((9))))
if 3 in numeros:
    print('O valor 3 apareceu na posição {}'.format(numeros.index(3)+1))
else:
    print('O valor 3 não existe na Tupla de números')
print('Os números pares foram: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')
