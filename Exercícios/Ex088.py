from random import randint
while True:
    jogo = list()
    total = list()
    quant = int(input('Qual a quantidade de jogos? '))
    for c in range(0, quant):
        for d in range(0, 6):
            jogo.append(randint(0, 60))
        total.append(jogo[:])
        jogo.clear()
    for i, v in enumerate(total):
        print(f'Jogo #{i+1}: ',end='')
        print(f'{v}')
    op = str(input('Deseja usar um novo número de jogos (S/N)? ')).upper().strip()
    if op[0] == 'N':
        break
print('Obrigado por usar o MEGASENA9000!')