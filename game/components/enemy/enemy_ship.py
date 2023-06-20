import pygame, random

from game.components.enemy.enemy import Enemy

from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_EXPLOSION

class EnemyShip(Enemy):
    def __init__(self):
        self.width = 40
        self.height = 50
        self.image = random.choice([ENEMY_2, ENEMY_1])
        self.image = pygame.transform.scale(self.image, (self.width, self.height))        
        self.sound = ENEMY_EXPLOSION
        super().__init__(self.image)