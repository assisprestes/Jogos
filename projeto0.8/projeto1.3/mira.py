import pygame
from pygame.sprite import Sprite

class Mira(Sprite):
    def __init__(self, ai_settings, screen, painel_vacina):
        super().__init__()
        self.painel_vacina = painel_vacina
        self.ai_settings = ai_settings
        self.screen = screen
        #Load imagem
        self.image = pygame.image.load('imagens/outros/mira.png')
        self.image = pygame.transform.scale(self.image, self.ai_settings.mira_tamanho)

        self.image_seringa = pygame.image.load('imagens/vacinas/vacina1.png')
        self.image_seringa = pygame.transform.scale(self.image_seringa, self.ai_settings.mira_tamanho)
        self.rect_seringa = self.image_seringa.get_rect()

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)



    def blitme(self):
        #desenha nave posição atual
        self.blit_mira()
        self.screen.blit(self.image_seringa,self.rect_seringa)
        
    def blit_mira(self):
        #desenha nave posição atual
        self.screen.blit(self.image,self.rect)

    def update_vacina_image(self):
        vacina_selecionada = self.painel_vacina.vacina_selecionada

        if vacina_selecionada == 0:
            self.image_seringa = pygame.image.load('imagens/vacinas/vacina1.png')
        elif vacina_selecionada == 1:
            self.image_seringa = pygame.image.load('imagens/vacinas/vacina2.png')
        elif vacina_selecionada == 2:
            self.image_seringa = pygame.image.load('imagens/vacinas/vacina3.png')
        elif vacina_selecionada == 3:
            self.image_seringa = pygame.image.load('imagens/vacinas/vacina4.png')

        self.image_seringa = pygame.transform.scale(self.image_seringa, self.ai_settings.mira_tamanho)
        self.rect_seringa = self.image_seringa.get_rect()

    def update(self):
        self.update_vacina_image()
        self.rect_seringa.topright = self.rect.center
        return 0