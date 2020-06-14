import pygame
from pygame.sprite import Sprite


class Limite_colisor(Sprite):
    """Classe para adiministrar os limites"""

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        # Retangulo do colisor
        self.rect = screen.get_rect()

    def update(self):
        return 0

    def draw_mira(self):
        pass
