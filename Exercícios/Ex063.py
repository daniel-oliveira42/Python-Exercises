#Fibonacci
lim = int(input('Limite da sequência: '))
c = 2
t1 = 0
t2 = 1
print(f'{t1} > {t2} ', end='')
while c < lim:
    t3 = t1 + t2
    print(' > {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
