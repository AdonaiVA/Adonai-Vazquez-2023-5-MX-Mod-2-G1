import pygame,random

from pygame.sprite import Sprite

from game.utils.constants import SHIELD, SCREEN_HEIGHT

class Shield(Sprite):
    def __init__(self): 
        self.width = 40
        self.height = 40
        self.image = SHIELD
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice([50, 100, 200, 250, 300, 400, 450, 500])
        self.rect.bottom = SCREEN_HEIGHT - 200

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        