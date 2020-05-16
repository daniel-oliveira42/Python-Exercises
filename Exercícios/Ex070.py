s = 0
sk = 0
c = 0
while True:
    np = str(input('Insira o nome do produto: ')).strip()
    pp = float(input(f'Qual o preço do produto {np}? '))
    s += pp
    if pp > 1000:
        sk += 1
    if c == 0:
        menor = pp
        nom_menor = np
    elif pp < menor:
        menor = pp
        nom_menor = np
    cont = str(input('Quer continuar (S/N)? ')).upper().strip()
    if cont == 'N':
        break
    c+=1
print(f'A soma foi de R${s:.2f}')
print(f'Houveram {sk} produtos com valor maior que 1000 reais')
print(f'O menor preço de produto foi o {nom_menor}')
