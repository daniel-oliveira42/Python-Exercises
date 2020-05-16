esc = int(input('Escolha entre: \n 1 - Binário \n 2 - Octal \n 3 - Hexadecimal \n\n Escreva aqui: '))

if esc == 1:
    num = int(input('Insira o número escolhido: '))
    print('{} em Binário é {}'.format(num, bin(num)[2:]))
elif esc == 2:
    num = int(input('Insira o número escolhido: '))
    print('{} em Octal é {}'.format(num, oct(num)[2:]))
elif esc == 3:
    num = int(input('Insira o número escolhido: '))
    print('{} em Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Insira uma opção válida')
