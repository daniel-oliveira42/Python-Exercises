import math

al = float(input('Escreva o ângulo: '))

s = math.sin(math.radians(al))
c = math.cos(math.radians(al))
t = math.tan(math.radians(al))

print('O seno é: {:.2f}'.format(s))
print('O cosseno é: {:.2f}'.format(c))
print('A tangente é: {:.2f}'.format(t))
