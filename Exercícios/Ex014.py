dia = int(input('Insira o número de dias utilizados '))
km = float(input('Insira o número de KM rodados '))
total = dia*60 + km*0.15

print('O total foi de R${:.2f}'.format(total))


