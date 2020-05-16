a = float(input('Insira o valor do primeiro lado do triângulo: '))
b = float(input('Insira o valor do segundo lado do triângulo: '))
c = float(input('Insira o valor do terceiro lado do triângulo: '))

if (a+b) > c and (a+c) > b and (b+c) > a:
    if a == b and b == c:
        tipo = 'EQUILÁTERO'
    elif a != b and b != c:
        tipo = 'ESCALENO'
    else:
        tipo = 'ISÓCELES'
    print('Triângulo {} possível'.format(tipo))
else:
    print('Triângulo impossível')