colunas = [[0,0,0],[0,0,0],[0,0,0]]

for c in range(0, 3):
    for d in range(0, 3):
        colunas[c][d] = int(input('Número: '))
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{colunas[c][d]:^5}]', end='')
    print()