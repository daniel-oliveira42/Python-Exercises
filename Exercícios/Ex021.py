from pygame import mixer

op = '0'

print('\nOlá meu querido amigo')
while op[0] != 'N':
  ht = '0'
  ht = str(input('Você está triste hoje? ')).strip().upper()
  mixer.init()
  mixer.pause()
  if ht[0] == 'S':
    mixer.init()
    mixer.music.load('fds.mp3')
    mixer.music.play()
    print('Não mais')
    op = str(input('Quer dar outra resposta? ')).strip().upper()

  elif ht[0] == 'N':
    mixer.init()
    mixer.music.load('trn.mp3')
    mixer.music.set_volume(0.3)
    mixer.music.play()
    print('Que bom! Que o dia continue feliz meu gigante pela própria natureza')
    op = str(input('Quer dar outra resposta? ')).strip().upper()
print('Volte sempre')
