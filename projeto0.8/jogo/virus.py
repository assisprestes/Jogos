import pygame
from pygame.sprite import Sprite
from pygame.sprite import groupcollide
from random import randint
from animacao import Animacao

# Classe fabrica vírus
class Virus(Sprite):
        # Fábrica de virus
    """Classe para adiministrar os vírus"""

    def __init__(self, ai_settings, screen, tipo_virus, estado_jogo):
        # cria virus
        super().__init__()
        self.ai_settings = ai_settings
        self.estado_jogo = estado_jogo
        self.screen = screen
        # Define dimensoes para o tipo especifico de virus
        self.largura = 150
        self.altura = 150
        self.tipo = tipo_virus
        # Retangulo do projetil
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)

        self.dimensao_tela = screen.get_rect().bottomright

        self.CIMA = 0
        self.CIMA_DIREITA = 1
        self.DIREITA = 2
        self.BAIXO_DIREITA = 3
        self.BAIXO = 4
        self.BAIXO_ESQUERDA = 5
        self.ESQUERDA = 6
        self.ESQUERDA_CIMA = 7

        self.direcao = self.CIMA # 0 -> cima, 1 -> cima_direita, 2 -> direita, 3 -> baixo_direita
                         # 4 -> baixo, 5 -> baixo_esquerda, 6 esquerda, 7 esquerda_cima

        if tipo_virus == "virus1":
                self.animacao = Animacao('./imagens/virus/Virus00', self.screen, self.largura, self.altura)
                # Carrega imagen do virus
                self.image = self.animacao.get_imagem()

                self.speed = self.ai_settings.speed1 * self.estado_jogo.nivel
        elif tipo_virus == "virus2":
                self.animacao = Animacao('./imagens/virus/Virus01', self.screen, self.largura, self.altura)
                # Carrega imagen do virus
                self.image = self.animacao.get_imagem()
                self.speed = self.ai_settings.speed2 * self.estado_jogo.nivel
        elif tipo_virus == "virus3":
                self.animacao = Animacao('./imagens/virus/Virus02', self.screen, self.largura, self.altura)
                # Carrega imagen do virus
                self.image = self.animacao.get_imagem()
                self.speed = self.ai_settings.speed3 * self.estado_jogo.nivel
        elif tipo_virus == "virus4":
                self.animacao = Animacao('./imagens/virus/Virus03', self.screen, self.largura, self.altura)
                # Carrega imagen do virus
                self.image = self.animacao.get_imagem()
                self.speed = self.ai_settings.speed4 * self.estado_jogo.nivel

        self.image = pygame.transform.scale(self.image, (self.largura, self.altura))

        self.rect = self.image.get_rect()

    def update(self):
        self.animacao.update()
        self.image = self.animacao.get_imagem()
            #colisao com a esquerda
        if self.rect.centerx < 0:
            self.update_direcao(1, 3)
            #colide com a direita
        elif self.rect.centerx > self.screen.get_rect().bottomright[0]:
            self.update_direcao(5, 7)
            #colide cima
        elif self.rect.centery < 100:
            self.update_direcao(2, 6)
            #colide embaixo
        elif self.rect.centery > self.screen.get_rect().bottomright[1] - 100:
            self.update_direcao(0, 2)

    def update_direcao(self, valor_minimo, valor_maximo):
        """ Define uma nova posição aleatoria."""
        self.direcao = randint(valor_minimo, valor_maximo)

    def mover(self):
        if not self.estado_jogo.pause:
            # cima
            if self.direcao == self.CIMA:
                self.rect.centery -= self.speed
            # cima_direita
            elif self.direcao == self.CIMA_DIREITA:
                self.rect.centerx += self.speed
                self.rect.centery -= self.speed
            # direita
            elif self.direcao == self.DIREITA:
                self.rect.centerx += self.speed
            # baixo_direita
            elif self.direcao == self.BAIXO_DIREITA:
                self.rect.centerx += self.speed
                self.rect.centery += self.speed
            # baixo
            elif self.direcao == self.BAIXO:
                self.rect.centery += self.speed
            # baixo_esquerda
            elif self.direcao == self.BAIXO_ESQUERDA:
                self.rect.centerx -= self.speed
                self.rect.centery += self.speed
            # esquerda
            elif self.direcao == self.ESQUERDA:
                self.rect.centerx -= self.speed
            # esquerda_cima
            elif self.direcao == self.ESQUERDA_CIMA:
                self.rect.centerx -= self.speed
                self.rect.centery -= self.speed


    def draw_virus(self):
        # pygame.draw.rect(self.screen, (200,52,148), self.rect)
        self.screen.blit(self.image, self.rect)
