import pygame

from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP


class Spaceship(Sprite):
    def __init__(self):
        self.width = 40
        self.height = 50
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, keyboard_events):
        pass