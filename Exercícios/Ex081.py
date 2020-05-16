op = ''
c = 0
numeros = []
while op != 'N':
    numeros.append(int(input('Digite o número: ')))
    op = str(input('Deseja continuar? ')).strip().upper()
numeros.sort(reverse=True)
print(f'Números: {numeros}')
if 5 in numeros:
    print('O valor 5 \033[1;32mESTÁ \033[mem números')
elif 5 not in numeros:
    print('O valor 5\033[1;31m NÃO\033[m está em números')
print(f'Você digitou {len(numeros)} número(s)')
