from math import pow

peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))

imc = peso/pow(altura, 2)
imc = round(imc, 1)

if imc < 18.5:
 print('Seu Índice de Massa Corporal é de {}, ou seja, você está abaixo do peso ideal para sua altura'.format(imc))
elif imc <= 24.9:
 print('Seu Índice de Massa Corporal é de {}, ou seja, você está com o peso ideal para sua altura'.format(imc))
elif imc <= 29.9:
 print('Seu Índice de Massa Corporal é de {}, ou seja, você está com sobrepeso para sua altura'.format(imc))
elif imc <= 34.9:
 print('Seu Índice de Massa Corporal é de {}, ou seja, você está no grau de Obesidade 1'.format(imc))
elif imc <= 40:
 print('Seu Índice de Massa Corporal é de {}, ou seja, você está no grau de Obesidade 2'.format(imc))
elif imc > 40:
 print('Seu Índice de Massa Corporal é de {}, ou seja, você está no grau de Obesidade 3'.format(imc))
else:
    print('Erro')
