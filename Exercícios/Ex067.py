num = 0
while True:
    n = int(input('\nInsira o número: '))
    if n < 0:
        break
    for c in range (1,11):
        tot = n*c
        print(f'{n}x{c} = {tot}')
    