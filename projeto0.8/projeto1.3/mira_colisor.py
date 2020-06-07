import pygame
from pygame.sprite import Sprite


class Mira_colisor(Sprite):
    """Classe para adiministrar os misséis"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.largura = 1
        self.altura = 1
        # Retangulo do projetil
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)

    def update(self):
        return 0

    def draw_mira(self):
        pygame.draw.rect(self.screen, (200, 52, 148), self.rect)
