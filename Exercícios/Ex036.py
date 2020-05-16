sal = float(input('Qual o seu salário? '))
anos = int(input('Em quanto tempo será efetuado o pagamento? '))
casa = float(input('Qual o valor da casa? '))

prest = casa/anos * 12

if prest <= sal*0.3:
    print('\033[1;92mEmpréstimo aprovado!')
else:
    print('\033[1;31mEmpréstimo negado')