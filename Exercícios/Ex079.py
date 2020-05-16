op = 0
numeros = []
while op != 'N':
    n = int(input('Escreva o número: '))
    if n in numeros:
        print('Número repetido, não o adicionei')
    else:
        numeros.append(n)
    op = str(input('Deseja continuar (S/N)? ')).strip().upper()
numeros.sort()
print(f'Os números em ordem são {numeros}')
