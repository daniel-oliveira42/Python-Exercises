palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')
vogais = ('a', 'e', 'i', 'o', 'u')

for c in palavras:
    print(f'\nA palavra {c} tem as seguintes vogais: ', end='')
    for letra in c:
        if letra.lower() in vogais:
            print(letra, end=' ')
