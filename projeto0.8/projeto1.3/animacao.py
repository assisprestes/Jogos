import os
import pygame


class Animacao:
    def __init__(self, pasta_imagens, screen, largura, altura):
        self.altura = altura
        self.largura = largura
        self.screen = screen
        self.imagens = []
        self.set_imagens(pasta_imagens)
        self.imagen_corrente = 0
        self.rect_screen = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.is_play = True
        self.fator_tempo = 1
        self.fator_tempo_aux = 0
        self.visivel = False

    def get_imagem(self):
        return pygame.transform.scale(self.imagens[self.imagen_corrente], (self.largura, self.altura))

    def set_imagens(self, pasta_imagens):
        paths_imagens = os.listdir(pasta_imagens)
        paths_imagens.sort()
        for path_imagen in paths_imagens:
            self.imagens.append(pygame.image.load(pasta_imagens + '/' + path_imagen))

    def update(self):
        self.fator_tempo_aux += 1
        if not self.fator_tempo_aux % self.fator_tempo:
            self.proxima_imagem()
        if self.visivel:
            self.blit()

    def play(self):
        self.is_play = True

    def stop(self):
        self.is_play = False

    def proxima_imagem(self):
        if self.is_play:
            if self.imagen_corrente < self.imagens.__len__() - 1:
                self.imagen_corrente += 1
            else:
                self.imagen_corrente = 0

    def blit(self):
        self.screen.blit(self.get_imagem(), self.rect)
