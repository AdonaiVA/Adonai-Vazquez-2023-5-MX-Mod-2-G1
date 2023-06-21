

class HandleColision:
    def __init__(self, starship, enemy_handler):
        self.starship_bullet = starship
        self.enemy_list = enemy_handler
    
    def collision(self):
        for enemy in self.enemy_list:
            for bullet in self.starship_bullet:
                if enemy.rect.colliderect(bullet.rect):
                    enemy.sound.play()
                    enemy.is_alive = False
        