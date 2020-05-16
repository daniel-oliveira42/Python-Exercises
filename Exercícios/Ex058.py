from random import randint
print('O PC pensou num número de 1 a 10, chute até acertar!')
pc_pensa = randint(1, 10)
jogador_chuta = int(input('\033[1;36mSeu chute: '))
c = 1
while pc_pensa != jogador_chuta:
    jogador_chuta = int(input('\033[1;31mErrou! Tente Novamente: '))
    c += 1
print('\033[1;92mAcertou! Parabéns!')
print('\033[mVocê precisou de {} tentativas!'.format(c))
