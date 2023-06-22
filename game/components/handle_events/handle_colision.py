class HandleColision:
    def __init__(self, starship, enemies, game_over_condition):
        self.starship = starship
        self.enemies = enemies
        self.game_over_condition = game_over_condition
        self.score = 0
        self.enemies_deleted = 0
        self.high_score = 0

    
    def collision_bullet_enemy(self):
        for enemy in self.enemies.enemies:
            for bullet in self.starship.bullets:
                if enemy.rect.colliderect(bullet.rect):
                    self.starship.bullets.remove(bullet)
                    enemy.sound.play()
                    enemy.is_alive = False
                    self.score += 100
                    self.enemies_deleted += 1
    
    def collision_bullet_starship(self):
        for enemy in self.enemies.enemies:
            for bullet in enemy.bullets:

                if bullet.rect.colliderect(self.starship):
                    enemy.bullets.remove(bullet)
                    self.starship.lives -= 1

    def check_game_over(self):
        if self.starship.lives == 0:
            self.starship.is_alive = False
            self.game_over_condition = True

    def update_high_score(self):
        if self.high_score < self.score:
            self.high_score = self.score
    
    def reset_score(self):
        self.score = 0

    def reset_enemies(self):
        self.enemies_deleted = 0            