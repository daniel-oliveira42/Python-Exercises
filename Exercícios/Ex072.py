numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
nomes = \
    ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
     'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenovoe', 'Vinte')
op = ''
while op != 'N':
    num = int(input('Insira um número de 0 a 20: '))
    if num not in numeros:
        while num not in numeros:
            num = int(input('Número inválido, escreva um número entre 0 e 20: '))
    print(f'O número se escreve: {nomes[num]}')
    op = str(input('Deseja escrever outro número (S/N): ')).upper().strip()
print('Obrigado pela preferência!')