numeros = [0, 0, 0, 0, 0]
mr_posição = mn_posição = maior = menor = 0
for c in range(0, 5):
    numeros[c] = int(input(f'Escreva o número #{c+1}: '))
    if c == 0:
        maior = numeros[c]
        menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
            mr_posição = c
        elif numeros[c] < menor:
            menor = numeros[c]
            mn_posição = c
print(f'O menor número foi {menor} na posição {mn_posição+1}')
print(f'O maior número foi {maior} na posição {mr_posição+1}')
