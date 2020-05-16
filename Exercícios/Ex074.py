from random import randint
maior = menor = 0
tupla_aleat = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
print(tupla_aleat)
for c in range(0,5):
    if c == 0:
        maior = tupla_aleat[c]
        menor = tupla_aleat[c]
    elif tupla_aleat[c] > maior:
        maior = tupla_aleat[c]
    elif tupla_aleat[c] < menor:
        menor = tupla_aleat[c]
print(f'Os seguintes número foram gerados: {tupla_aleat}, sendo {maior} o maior e {menor} o menor')

#Outras opções para maior e menor e impressão de tupla:
#max(tupla_aleat) e min(tupla_aleat)
#for n in tupla_aleat:
#   print(n, end=' ')