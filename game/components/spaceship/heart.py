import pygame

from pygame.sprite import Sprite

from game.utils.constants import HEART, SCREEN_HEIGHT, SCREEN_WIDTH

class Heart(Sprite):
    def __init__(self):
        self.width = 20
        self.height = 20
        self.image = HEART
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = SCREEN_HEIGHT - 30

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

