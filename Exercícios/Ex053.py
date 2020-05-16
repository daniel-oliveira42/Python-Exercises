frase = str(input('Escreva a frase que você quer testar: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto)-1, -1, -1):
    inverso += junto[c]

if inverso == junto:
    print('É palíndromo')
else:
    print('Não é palíndromo!')
