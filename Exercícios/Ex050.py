s = 0
for c in range(1,6):
    print('Insira o número #{}: '.format(c), end='')
    n = int(input(''))
    if n % 2 == 0:
     s = s + n
print('Soma = ', s)