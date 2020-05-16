idade = int(input('Insira sua idade: '))

if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('CATEGORIA JÚNIOR')
elif idade <= 25:
    print('CATEGORIA SENIOR')
else:
    print('CATEGORIA MASTER')