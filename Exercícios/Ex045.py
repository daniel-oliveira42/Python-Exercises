from random import randint

joga_pc = randint(0, 2)

#0 - Pedra // 1 - Papel 2 // - Tesoura

print('O PC está preparado! Qual a sua jogada?')
joga_vc = int(input('\n[0] - Pedra \n[1] - Papel \n[2] - Tesoura\n\n'))
jogadas = ['Pedra','Papel','Tesoura']

if joga_pc == joga_vc:
    print('O pc jogou {} e você jogou {}! EMPATE!'.format(jogadas[joga_pc],jogadas[joga_pc]))
elif joga_pc == 2 and joga_vc == 1:
    print('O pc jogou {}! \n \033[1;31mVocê Perdeu!'.format(jogadas[joga_pc]))
elif joga_pc == 2 and joga_vc == 0:
    print('O pc jogou {}! \n \033[1;92mVocê Ganhou!'.format(jogadas[joga_pc]))
elif joga_pc == 1 and joga_vc == 2:
    print('O pc jogou {}! \n \033[1;92mVocê Ganhou!'.format(jogadas[joga_pc]))
elif joga_pc == 1 and joga_vc == 0:
    print('O pc jogou {}! \n \033[1;31mVocê Perdeu!'.format(jogadas[joga_pc]))
elif joga_pc == 0 and joga_vc == 2:
    print('O pc jogou {}! \n \033[1;31mVocê Perdeu!'.format(jogadas[joga_pc]))
elif joga_pc == 0 and joga_vc == 1:
    print('O pc jogou {}! \n \033[1;92mVocê Ganhou!'.format(jogadas[joga_pc]))
else:
    print('\033[4;31mInsira uma opção válida! (0 a 2!)')

