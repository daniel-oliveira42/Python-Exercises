from random import randint

c = 0
while True:
    pi_vc = str(input('Escolha par ou ímpar [P/I]: '))
    joga_vc = int(input('Qual o número que você vai jogar (1 a 10)?  '))
    joga_pc = randint(1, 10)
    jogo = joga_vc + joga_pc
    if pi_vc == 'P':
        if jogo % 2 == 0:
            print('Você ganhou!')
            c += 1
        else:
            print('Você perdeu!')
            break
    if pi_vc == 'I':
        if jogo % 2 == 0:
            print('Você perdeu')
            break
        else:
            print('Você ganhou!')
            c += 1
print(f'Você ganhou {c} partida(s) seguida(s)')
