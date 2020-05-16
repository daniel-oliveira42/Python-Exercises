expressão = str(input('Escreva a expressão: '))
pilha = []
for parenteses in expressão:
    if parenteses == '(':
        pilha.append('(')
    elif parenteses == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')