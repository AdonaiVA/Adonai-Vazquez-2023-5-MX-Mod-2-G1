import random

from game.components.enemy.enemy_bullet import Bullet

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, ENEMY_SHOOT_SOUND

class Enemy:
    def __init__ (self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([100, 150, 200, 250, 300, 350, 400, 450, 500, 550])
        self.rect.y = 0
        self.speed_x = random.choice([10,15])
        self.speed_y = 50
        self.LEFT = "left"
        self.RIGHT = "right"
        self.mov_x = random.choice([self.LEFT, self.RIGHT])
        self.is_alive = True
        self.index = 0
        self.bullets = []
        self.sound = ENEMY_SHOOT_SOUND

    def update(self):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        self.move()
        self.shoot()
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        for bullet in self.bullets:
            screen.blit(bullet.image, bullet.rect)

    def move(self):
        if self.mov_x == self.RIGHT:
            self.rect.x += self.speed_x
            if self.rect.x > SCREEN_WIDTH - 50:
                self.rect.y += self.speed_y
                self.mov_x = self.LEFT
                self.index += 1
        else:
            self.rect.x -= self.speed_x
            if self.rect.x <= 0:
                self.rect.y += self.speed_y
                self.mov_x = self.RIGHT
                self.index += 1
    
    def shoot(self):
        if random.randrange(0, 10) == 1:
            bullet = Bullet(self.rect)
            self.bullets.append(bullet)
            #self.sound.play()

        for bullet in self.bullets:
            bullet.update()
            if not bullet.available:
                self.bullets.remove(bullet)




