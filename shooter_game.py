from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.retc.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
speed = 0.9
class Monsters(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = transform.scale(image.load(player_image))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.retc.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image())
class Bullet(GameSprite):
    def update(self):
            while self.rect.y<0:
                self.rect.y -= speed

display.set_caption("Maze")
background = transform.scale(image.load("galaxy.jpg"), (700,500))
mixer.init()
mixer.music.load('newer-wave-by-kevin-macleod-from-filmmusic-io.mp3')
mixer.music.play()

for i in range(20):
    vrag = Enemy(ufo.png, randint(1, 700), 0, 15,)
    monsers.add(vrag)

