import pygame

from game.utils.constants import FONT_STYLE


class Score:
    def __init__(self):
        self.font = pygame.font.Font(FONT_STYLE, 25)
        self.record = 0
        self.x_position = 10
        self.y_position = 10

    def update(self, score):
        self.record = score

    def draw(self, screen):
        score_text = self.font.render(f'Score: {self.record}', True, (255, 255, 255))
        screen.blit(score_text, (self.x_position, self.y_position))
