from random import randint

print('Pensei em um número de 0 a 5, tente adivinha-lo')
chute = int(input('O número é: '))

num = randint(0, 5)

if chute == num:
    print('Parabéns, você acertou! O numero era ', num)
else:
    print('Errouuu, o número era ', num)
