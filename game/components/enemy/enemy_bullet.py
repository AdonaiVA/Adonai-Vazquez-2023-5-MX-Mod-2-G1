import pygame

from pygame.sprite import Sprite

from game.utils.constants import BULLET_ENEMY, BULLET_SOUND

class Bullet(Sprite):
    def __init__(self, enemy):
        self.width = 10
        self.height = 20
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = enemy.centerx
        self.rect.y = enemy.bottom
        self.speed = 10
        self.available = True
        self.sound = BULLET_SOUND

    def update(self):
        self.move()

    def move(self):
        self.rect.y += self.speed
        if self.rect.bottom <= 0:
            self.available = False
            return self.available
        else:
            return self.available
        