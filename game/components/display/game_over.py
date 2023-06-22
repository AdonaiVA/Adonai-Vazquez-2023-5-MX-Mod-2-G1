import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class GameOver:
    def __init__(self):
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render("Game Over. Press any key to resart", True, (250,0,0))
        self.text_width = self.text.get_width()
        self.text_height = self.text.get_height()
        self.text_x = (SCREEN_WIDTH // 2) - (self.text_width // 2) 
        self.text_y = (SCREEN_HEIGHT // 2) - (self.text_height)
        
    def draw(self,screen):
        screen.blit(self.text,(self.text_x, self.text_y))
        
    def draw_score(self, screen, score):
        score_text = self.font.render(f'Score: {score}', True, (255, 255, 255))
        score_text_width = score_text.get_width()
        screen.blit(score_text, ((SCREEN_WIDTH // 2) - (score_text_width // 2), self.text_y + self.text_height))

    def draw_enemies(self, screen, enemies):
        enemy_deleted = self.font.render(f'Enemy deleted: {enemies}', True, (255,255,255))
        enemy_deleted_width = enemy_deleted.get_width()
        screen.blit(enemy_deleted, ((SCREEN_WIDTH // 2) - (enemy_deleted_width // 2), self.text_y + (self.text_height * 2)))
