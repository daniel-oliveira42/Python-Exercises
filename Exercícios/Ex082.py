op = 0
numeros=[]
pares = []
impares = []
while op != 'N':
    numeros.append(int(input('Escreva o número: ')))
    op = str(input('Deseja continuar (S/N)? ')).strip().upper()
for i,v in enumerate(numeros):
    if v%2==0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Vetor: {numeros}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')