cart = float(input('Quanto dinheiro tem na carteira? (em reais) '))

pc = cart//3.27
qs = cart%3.27
qs = round(qs,2)
pc = int(pc)
print('Você pode comprar {} dólares, sobrando R${} reais na carteira '.format(pc,qs))