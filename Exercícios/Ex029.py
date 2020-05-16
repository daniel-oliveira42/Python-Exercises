vel = float(input('Insira a velocidade (em Km/h): '))

if vel > 80:
    excesso = vel - 80
    multa = excesso * 7
    print('Vocé foi multado por excesso de {} km na velocidade. A multa é de R${:.2f}'.format(int(excesso), multa))
else:
    print('Não houve infração! Continue dirigindo com segurança, parabéns!')
