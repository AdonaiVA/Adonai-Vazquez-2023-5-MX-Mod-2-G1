class HandleColision:
    def __init__(self, starship, enemies):
        self.starship = starship
        self.enemies = enemies
        self.score = 0

    
    def collision_bullet_enemy(self):
        for enemy in self.enemies.enemies:
            for bullet in self.starship.bullets:
                if enemy.rect.colliderect(bullet.rect):
                    enemy.sound.play()
                    enemy.is_alive = False
                    self.score += 100
    