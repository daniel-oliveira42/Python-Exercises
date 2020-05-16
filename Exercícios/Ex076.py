lista = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livros', 34.90)
print('='*37)
[print(f'{"Lista de Materiais":^37}')]
print('='*37)
for c in lista:
    if lista.index(c) % 2 == 0:
        print('{:.<30}'.format(lista[lista.index(c)]), end='')
    else:
        print(' {:>3.2f}'.format(lista[lista.index(c)]))