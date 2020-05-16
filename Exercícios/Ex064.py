c = 1
num = int(input('Escreva um número (999 pra parar): '))
soma = num
while num != 999:
    num = int(input('Escreva o próximo número (999 pra parar): '))
    if num != 999:
        soma += num
        c += 1
print(f'{c} números foram digitados')
print(f'A soma é: {soma}')
