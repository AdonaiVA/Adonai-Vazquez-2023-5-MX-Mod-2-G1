import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

from game.components.spaceship.spaceship import Spaceship

from game.components.enemy.enemy_handler import EnemyHandler

from game.components.handle_events.handle_colision import HandleEvents

from game.components.display.score import Score

from game.components.display.game_over import GameOver

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_over = False
        self.game_speed = 10 # el numero de pixeles que el "objeto / imagen" se mueve en patalla
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.spaceship = Spaceship()
        self.enemies_handler = EnemyHandler()
        self.events = HandleEvents(self.spaceship, self.enemies_handler, self.playing)
        self.score = Score()
        self.game_over_screen = GameOver()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
        else:
            print("Something occurred to quit the game!")
            
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        # pygame.event.get() es un iterable (lista)           
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #el QUIT event es el click en el icono que cierra ventana
                self.playing = False

            if self.game_over and event.type == pygame.KEYDOWN:
                self.restart_game()

    def update(self):
        if self.game_over:
            return
        else:
            events = pygame.key.get_pressed()
            self.spaceship.update(events)
            self.enemies_handler.update()

            self.events.collision_bullet_enemy()
            self.events.collision_bullet_starship()
            self.events.collision_enemy_spaceship()
            self.events.collision_shield_enemy()
            self.events.update_high_score()
            self.events.check_shield()

            self.score.update(self.events.score)
            self.events.check_game_over()
            print(self.spaceship.lives)
            if not self.spaceship.is_alive:
                self.game_over = True


    def draw(self):

        self.clock.tick(FPS) # configuro cuantos frames per second voy a dibujar            self.screen.fill((255, 255, 255)) # lleno el screen de color BLANCO???? 255, 255, 255 es el codigo RGB
        self.draw_background()            
        
        if self.game_over:
            self.game_over_screen.draw(self.screen)
            self.game_over_screen.draw_score(self.screen, self.score.record)
            self.game_over_screen.draw_enemies(self.screen, self.events.enemies_deleted)
            self.game_over_screen.draw_high_score(self.screen, self.events.high_score)
        else:
            self.spaceship.draw(self.screen)
            self.enemies_handler.draw(self.screen)
            self.score.draw(self.screen)

        pygame.display.update() # esto hace que el dibujo se actualice en el display de pygame
        pygame.display.flip()  # hace el cambio


    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()# alto de la imagen
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg)) # blit "dibuja"
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
    
    def restart_game(self):
        self.playing = True
        self.game_over = False
        self.spaceship.reset()
        self.events.reset_score()
        self.events.reset_enemies()
        self.enemies_handler.reset_enemies()
