import pygame
from pygame.sprite import Sprite


class Barra_tempo(Sprite):
    """Classe para adiministrar os misséis"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.tamanho_barra =  self.screen.get_rect().right - 320
        self.tamanho_maximo = self.tamanho_barra
        self.rect = pygame.Rect(300, 0, self.tamanho_barra , 20)
        self.rect.centery = 35
        self.color = (0, 255, 0)
        self.fator_divisao_barra = self.tamanho_barra / 3
        self.barra_vazia = False
        self.fator_decressimo = 0.0125 # Valor em segundos. Quanto menor mais rapido a barra acaba

    def atualiza_barra(self):
        if self.tamanho_barra > 0:
            self.tamanho_barra -= 1
        else:
            self.barra_vazia = True

        self.rect = pygame.Rect(300, 0, self.tamanho_barra, 20)
        self.rect.centery = 35

        if self.tamanho_barra < (self.fator_divisao_barra * 2) and self.tamanho_barra > self.fator_divisao_barra:
            self.color = ( 255, 255, 0)
        elif self.tamanho_barra < self.fator_divisao_barra:
            self.color = ( 200, 0, 0)

    def update(self):
        self.atualiza_barra()


    def desenha_barra(self, screen):
        """Desenha o missél na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def redefine_barra_tempo(self):
        self.tamanho_barra = self.tamanho_maximo
        self.color = (0, 255, 0)
