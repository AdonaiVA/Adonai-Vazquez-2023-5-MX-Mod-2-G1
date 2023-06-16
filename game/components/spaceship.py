import pygame

from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH


class Spaceship(Sprite):
    def __init__(self):
        self.width = 40
        self.height = 50
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.speed = 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, SCREEN_HEIGHT - 50))

    def update(self, keyboard_events):
        if keyboard_events[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif keyboard_events[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.width:
            self.rect.x += self.speed