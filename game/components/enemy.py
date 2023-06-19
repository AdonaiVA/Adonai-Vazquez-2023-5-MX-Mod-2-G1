import pygame, random

from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(Sprite):
    def __init__ (self, type):
        self.type = type
        self.width = 40
        self.height = 50
        self.image = random.choice([ENEMY_1,ENEMY_2])
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH-self.width)
        self.rect.y = 0
        self.speed = 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, playing):
        if self.type == "Horizontal":     
            self.move_horizontal(playing)
        elif self.type == "Vertical": 
            self.move_vertical(playing)


    def move_vertical(self, playing):
        if playing:
            self.rect.y += self.speed
            
            if self.rect.y > SCREEN_HEIGHT:
                self.rect.y = 0
                self.rect.x = random.randint(0, SCREEN_WIDTH)
            elif self.rect.y < 0:
                self.rect.y = SCREEN_HEIGHT 

    def move_horizontal(self, playing):
        if playing:
            self.rect.x += self.speed
            
            if self.rect.x > SCREEN_WIDTH:
                self.rect.x = 0
                self.rect.y += self.height
                    
                if self.rect.y > SCREEN_HEIGHT:
                    self.rect.y = 0

            elif self.rect.x < 0:
                self.rect.x = SCREEN_WIDTH
                
        


