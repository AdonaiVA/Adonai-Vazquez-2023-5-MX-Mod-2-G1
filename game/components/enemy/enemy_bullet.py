import pygame

from pygame.sprite import Sprite

from game.utils.constants import BULLET_ENEMY, SCREEN_HEIGHT

class Bullet(Sprite):
    def __init__(self, enemy_rect):
        self.width = 10
        self.height = 20
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = enemy_rect.centerx
        self.rect.y = enemy_rect.bottom
        self.speed = 10
        self.available = True

    def update(self):
        self.move()

    def move(self):
        self.rect.y += self.speed
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.available = False
