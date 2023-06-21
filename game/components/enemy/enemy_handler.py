import random, pygame

from game.components.spaceship.bullet import Bullet

from game.components.enemy.enemy_ship import EnemyShip

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.max_enemies = random.choice([5,3,6])
    
    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if not enemy.is_alive:
                self.remove_enemy(enemy)
        
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        
    def add_enemy(self):
        if len(self.enemies) < self.max_enemies:
            self.enemies.append(EnemyShip())
        
    def remove_enemy(self,enemy):
        self.enemies.remove(enemy)
    