num = int(input('Escreva um número: '))
dividiu = 0
for c in range(num, 0, -1):
    if num % c == 0:
        dividiu = dividiu + 1
if dividiu == 2:
    print('O número é primo')
else:
    print('O número não é primo')
