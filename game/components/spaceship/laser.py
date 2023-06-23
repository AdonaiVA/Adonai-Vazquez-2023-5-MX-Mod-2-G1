import pygame

from pygame.sprite import Sprite

from game.utils.constants import MEGA_LASER, SCREEN_HEIGHT

class MegaLaser:
    def __init__(self, starship):
        self.width = 80
        self.height = SCREEN_HEIGHT - starship.height
        self.image = MEGA_LASER
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = starship.centerx
        self.rect.y = starship.top

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
    