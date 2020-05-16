op = ''
soma = 0
c = 0
while op != 'N':
    num = int(input('Insira um número: '))
    soma += num
    c += 1
    if c == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    op = str(input('Deseja inserir outro valor? [S/N] ')).upper().strip()
print(f'A média entre os números é: {soma/c:.2f}')
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')