dados = list()
lista = list()
pesados = list()
leves = list()
op = ' '
c = 0
maisp = menosp = 0
nomesp = ' '
nomenosp = ' '

while op[0] != 'N':
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    op = str(input('Deseja continuar (S/N)? ')).upper().strip()
    if len(lista)==0:
        maisp = menosp = dados[1]
    else:
        if dados[1] > maisp:
            maisp = dados[1]
            nomesp = dados[0]
        if dados[1] < menosp:
            menosp = dados[1]
            nomenosp = dados[0]
    lista.append(dados[:])
    dados.clear()
print(f'Foram cadastradas {len(lista)} pessoas')
for i, c in enumerate(lista):
    if c[1] == maisp:
        print(f'Pesado: {lista[i]}')
    elif c[1] == menosp:
        print(f'Leve: {lista[i]}')
