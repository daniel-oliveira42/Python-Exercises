n1 = float(input('Insira sua nota 1: '))
n2 = float(input('Insira sua nota 1: '))

media = (n1+n2)/2
if media < 5:
    print('\033[;31mReprovado!')
elif media < 7.0:
    print('\033[;33mRecuperação!')
else:
    print('\033[;92mAprovado!')