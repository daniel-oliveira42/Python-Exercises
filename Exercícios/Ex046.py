from pygame import mixer
from time import sleep
import emoji

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':fireworks:')*10)
mixer.init()
mixer.music.load('frwks.mp3')
mixer.music.set_volume(0.3)
mixer.music.play()
input('')