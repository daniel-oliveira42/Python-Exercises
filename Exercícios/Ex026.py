frase = str(input('Insira a frase em questão: ')).strip()

print('A letra A aparece {} vezes'.format(frase.count('A')))
print('Primeira posição de A: {}'.format(frase.find('A')+1))
print('Última posição de A: {}'.format(frase.rfind('A')+1))

