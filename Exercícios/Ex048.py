s = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        s = s + c
print('A soma é igual a: ', s)