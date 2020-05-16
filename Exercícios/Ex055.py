for c in range(1, 6):
    print('Insira o peso {}: '.format(c), end='')
    peso = float(input(''))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior é: ', maior)
print('O menor é: ', menor)