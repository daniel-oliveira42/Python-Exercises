num = int(input('Escreva o número para ver seu fatorial: '))
c = num - 1
while c > 0:
    print(' {} '.format(c+1), end='')
    print(' x ', end='')
    if c == 1:
        print(c, end='')
    num = c*num
    c -= 1
print(' =', num)
