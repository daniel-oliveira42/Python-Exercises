pb = float(input('Insira o preço base do produto: '))
esc = int(input('Escolha a forma de pagamento: \n 1 - Á Vista/Cheque \n 2 - No Cartão \n 3 - Parcelado \n '))

if esc == 1:
    pf = pb - pb * 0.1
    print('O total foi de R&{:.2f}'.format(pf))
elif esc == 2:
    pf = pb - pb * 0.05
    print('O total foi de R&{:.2f}'.format(pf))
elif esc == 3:
    parcelas = int(input('Em quantas parcelas pretende pagar? '))
    if parcelas == 2:
        print('O valor total será de {:.2f} tendo {} parcelas de {:.2f} por mês'.format(pb, parcelas, pb / 2))
    elif parcelas >= 3:
        pf = pb + pb*0.2
        print('O valor total será de {:.2f} tendo {} parcelas de {:.2f} por mês'.format(pf, parcelas, pf / parcelas))
else:
    print('Digite uma opção válida')
