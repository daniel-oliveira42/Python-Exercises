c = -1
n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
while(c != 5):
    c = int(input('\n[1] - Somar \n[2] - Multiplicar \n[3] - Maior \n[4] - Novos números \n[5] - Sair do programa \n\n '))
    if c == 1:
        resultado = n1 + n2
    elif c == 2:
        resultado = n1 * n2
    elif c == 3:
        if n1 > n2:
            resultado = n1
        else:
            resultado = n2
    elif c == 4:
        n1 = int(input('Escreva um novo número: '))
        n2 = int(input('Escreva outro novo número: '))
    elif c == 5:
        print('Obrigado por usar meu programa!')
    else:
        print('Insira uma opção válida!!')
    if c != 5:
        print('O resultado da operação foi: {}'.format(resultado))
