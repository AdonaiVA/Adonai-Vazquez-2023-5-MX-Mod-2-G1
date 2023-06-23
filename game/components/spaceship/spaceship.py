import pygame, random

from pygame.sprite import Sprite

from game.components.spaceship.bullet import Bullet

from game.components.spaceship.heart import Heart

from game.components.spaceship.shield import Shield

from game.components.spaceship.laser import MegaLaser

from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP_EXPLOSION

class Spaceship(Sprite):
    def __init__(self):
        self.width = 40
        self.height = 50
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y =  SCREEN_HEIGHT - self.height
        self.speed = 10
        self.bullets = []
        self.lives = 3
        self.is_alive = True
        self.hearts = [Heart(10), Heart(40), Heart(70)]
        self.shield = Shield()
        self.have_shield = False
        self.explosion_sound = SPACESHIP_EXPLOSION

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        for bullet in self.bullets:
            screen.blit(bullet.image, bullet.rect)
        for heart in self.hearts:
            heart.draw(screen)
        if self.have_shield == True:   
            self.shield.draw(screen)

    def update(self, keyboard_events):
        self.move_left(keyboard_events)
        self.move_right(keyboard_events)
        self.move_up(keyboard_events)
        self.move_down(keyboard_events)
        self.shoot(keyboard_events)
        self.update_bullets()
        self.update_hearts()
        if self.have_shield == True:    
            self.update_shield()

        
    def move_left(self, keyboard_events):   
        if keyboard_events[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

    def move_right(self, keyboard_events):
        if keyboard_events[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.width:
            self.rect.x += self.speed
    
    def move_up(self, keyboard_events):
        if keyboard_events[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

    def move_down(self, keyboard_events):
        if keyboard_events[pygame.K_DOWN] and self.rect.y < SCREEN_HEIGHT - self.height:
            self.rect.y += self.speed
    
    def shoot(self, keyboard_events):
        if keyboard_events[pygame.K_SPACE]:
            bullet = Bullet(self.rect)
            self.bullets.append(bullet)
            bullet.sound.play()
            
    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()
            if not bullet.available:
                self.bullets.remove(bullet)
    
    def update_hearts(self):
        if self.lives == 2 and len(self.hearts) >= 3:
            self.hearts.pop()
        elif self.lives == 1 and len(self.hearts) >= 2:
            self.hearts.pop()
    
    def update_shield(self):
        if random.randrange(0,200) == 1:
            self.have_shield = False

            
    def reset(self):
        self.is_alive = True
        self.lives = 3
        self.hearts = [Heart(10), Heart(40), Heart(70)]
        

