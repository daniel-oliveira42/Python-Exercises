num = int(input('Digite um número (de 0 a 9999): '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando: {} '.format(num))
print('Milhares: {} '.format(m))
print('Centenas: {} '.format(c))
print('Dezenas: {} '.format(d))
print('Unidades: {} '.format(u))

