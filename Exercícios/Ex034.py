sal = float(input('Qual seu salário? '))

if sal > 1250:
    novo_sal = sal + (sal*0.1)
else:
    novo_sal = sal + (sal*0.15)
print('O novo salário será de {}'.format(novo_sal))