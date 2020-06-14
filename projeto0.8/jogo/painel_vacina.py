import pygame
from pygame.sprite import Sprite


class Painel_vacina(Sprite):
    """Classe para adiministrar os misséis"""

    def __init__(self, ai_settings, screen):
        # cria missél na posição da nave
        super().__init__()
        self.screen = screen
        # aqui o indice 0 representaa a vacina_1 assim como o indice 1 representa a vacina_2 e assim sucessivamente.
        self.vacinas = ['vacina1', 'vacina2', 'vacina3', 'vacina4']
        # Retangulo do projetil
        self.rect = pygame.Rect(ai_settings.screen_width - (ai_settings.painel_largura + ai_settings.painel_dist_borda), ai_settings.screen_height - (ai_settings.painel_altura + ai_settings.painel_dist_borda), ai_settings.painel_largura, ai_settings.painel_altura)
        self.color = ai_settings.painel_vacina_cor

        self.vacina_selecionada = ai_settings.painel_vacina_padrao


        #Load imagem das vacinas
        self.vacina_1 = pygame.image.load('imagens/vacinas/vacina1.png')
        self.vacina_1 = pygame.transform.scale(self.vacina_1, ai_settings.painel_tamanho_vacina)
        self.vacina_1 = pygame.transform.rotate(self.vacina_1, 45)
        self.fator_sel_vacina1 = 0

        self.vacina_2 = pygame.image.load('imagens/vacinas/vacina2.png')
        self.vacina_2 = pygame.transform.scale(self.vacina_2, ai_settings.painel_tamanho_vacina)
        self.vacina_2 = pygame.transform.rotate(self.vacina_2, 45)
        self.fator_sel_vacina2 = 0

        self.vacina_3 = pygame.image.load('imagens/vacinas/vacina3.png')
        self.vacina_3 = pygame.transform.scale(self.vacina_3, ai_settings.painel_tamanho_vacina)
        self.vacina_3 = pygame.transform.rotate(self.vacina_3, 45)
        self.fator_sel_vacina3 = 0


        self.vacina_4 = pygame.image.load('imagens/vacinas/vacina4.png')
        self.vacina_4 = pygame.transform.scale(self.vacina_4, ai_settings.painel_tamanho_vacina)
        self.vacina_4 = pygame.transform.rotate(self.vacina_4, 45)
        self.fator_sel_vacina4 = 0

    def update(self, ai_settings):
        if self.vacina_selecionada == 0:
            self.fator_sel_vacina1 = ai_settings.painel_fator_selecao
            self.fator_sel_vacina2 = 0
            self.fator_sel_vacina3 = 0
            self.fator_sel_vacina4 = 0
        elif self.vacina_selecionada == 1:
            self.fator_sel_vacina1 = 0
            self.fator_sel_vacina2 = ai_settings.painel_fator_selecao
            self.fator_sel_vacina3 = 0
            self.fator_sel_vacina4 = 0
        elif self.vacina_selecionada == 2:
            self.fator_sel_vacina1 = 0
            self.fator_sel_vacina2 = 0
            self.fator_sel_vacina3 = ai_settings.painel_fator_selecao
            self.fator_sel_vacina4 = 0
        elif self.vacina_selecionada == 3:
            self.fator_sel_vacina1 = 0
            self.fator_sel_vacina2 = 0
            self.fator_sel_vacina3 = 0
            self.fator_sel_vacina4 = ai_settings.painel_fator_selecao


    def desenha_painel_vacina(self, ai_settings, screen):
        """Desenha o missél na tela"""
        pygame.draw.lines(self.screen, self.color, True, [self.rect.topleft,self.rect.topright, self.rect.bottomright, self.rect.bottomleft], ai_settings.painel_largura_borda)#rect(self.screen, self.color, self.rect)
        screen.blit(self.vacina_1, pygame.Rect(self.rect.x -40, self.rect.y - self.fator_sel_vacina1, self.vacina_1.get_rect().bottomright[0],  self.vacina_1.get_rect().bottomright[1]))
        screen.blit(self.vacina_2, pygame.Rect(self.rect.x + 20, self.rect.y - self.fator_sel_vacina2, self.vacina_2.get_rect().bottomright[0],  self.vacina_1.get_rect().bottomright[1]))
        screen.blit(self.vacina_3, pygame.Rect(self.rect.x + 85, self.rect.y - self.fator_sel_vacina3, self.vacina_3.get_rect().bottomright[0],  self.vacina_1.get_rect().bottomright[1]))
        screen.blit(self.vacina_4, pygame.Rect(self.rect.x + 155, self.rect.y - self.fator_sel_vacina4, self.vacina_4.get_rect().bottomright[0],  self.vacina_1.get_rect().bottomright[1]))
