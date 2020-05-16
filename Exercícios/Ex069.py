homens=0
abaixo20=0
c=0
while True:
    sexo = str(input('Qual seu sexo [M/F]? ')).strip().upper()
    idade = int(input('Qual sua idade? '))
    if idade > 18:
        c += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        abaixo20 += 1
    cont = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if cont == 'N':
        break
print(f'Tem {homens} homens cadastrados')
print(f'Tem {c} pessoas acima de 18 anos')
print(f'Tem {abaixo20} mulheres abaixo dos 20 anos')