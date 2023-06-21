import pygame

from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_SOUND

class Bullet(Sprite):
    def __init__(self, rect_spaceship):
        self.width = 10
        self.height = 20
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = rect_spaceship.centerx
        self.rect.y = rect_spaceship.y
        self.speed = 10
        self.available = True
        self.sound = BULLET_SOUND

    def update(self):
        self.move()


    def move(self):
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            self.available = False
