contm20 = 0
total_idade = 0
nome_maior = ''
for c in range(0,4):
    print('Pessoa {}'.format(c+1))
    nome = str(input('Escreva o seu nome: '))
    idade = int(input('Escreva sua idade: '))
    sexo = str(input('Escreva seu sexo [M/F]: ')).upper().strip()
    if sexo == 'M':
        if c == 0:
            maior = idade
            nome_maior = nome
        if idade > maior:
            maior = idade
            nome_maior = nome
    if sexo == 'F':
        if idade < 20:
            contm20 += 1
    total_idade += idade
print(f'O nome do homem mais velho é {nome_maior} com {maior} anos')
print(f'Existem {contm20} mulheres com menos de 20 anos')
print(f'A média das idades é de {total_idade/4} anos')