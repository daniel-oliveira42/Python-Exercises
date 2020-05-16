dist = float(input('Insira a distância do destino em Km: '))
if dist <= 200:
    preço = dist * 0.5
    print('O preço final da viagem foi de R${:.2f} '.format(preço))
else:
    preço = dist * 0.45
    print('O preço final da viagem foi de R${:.2f}'.format(preço))