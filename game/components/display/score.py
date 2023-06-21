import pygame

from pygame import font

from game.utils.constants import FONT_STYLE


class Score:
    def __init__(self, score):
        self.font = pygame.font.Font(FONT_STYLE, 25)
        self.record = score

    def update(self, score):
        self.record = score

    def draw(self, screen):
        score_text = self.font.render(f'Score: {self.record}', True, (255, 255, 255))
        screen.blit(score_text, (0, 0))