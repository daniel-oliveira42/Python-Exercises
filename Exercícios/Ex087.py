colunas = [[0,0,0],[0,0,0],[0,0,0]]
sp = 0
tc = 0
maior = 0
for d in range(0, 3):
    for c in range(0, 3):
        colunas[c][d] = int(input('Número: '))
        if d == 2:
            tc += colunas[c][d]
        if colunas[c][d] % 2 == 0:
            sp += colunas[c][d]
        if c == 1:
            for c in range(0,3):
                if c == 1:
                    maior = colunas[c][d]
                elif colunas[c][d] > maior:
                    maior = colunas[c][d]
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{colunas[c][d]:^5}]', end='')
    print()
print(f'Soma dos pares: {sp}')
print(f'Soma dos valores da terceira coluna: {tc}')
print(f'O maior valor da segunda linha é: {maior}')
