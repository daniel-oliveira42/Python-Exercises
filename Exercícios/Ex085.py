lista = [[], []]
for c in range(1, 8):
    n = int(input(f'Informe o valor #{c}: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'Pares: {sorted(lista[0])}')
print(f'Impares: {sorted(lista[1])}')
