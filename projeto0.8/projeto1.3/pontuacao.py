import pygame.font

class Pontuacao():
    """ Classe para exibir pontuação"""
    def __init__(self, ai_settings,screen, estado_jogo):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.estado_jogo = estado_jogo
        
        self.cor_texto = (30, 30, 30)
        self.fonte = pygame.font.SysFont(None, 48)
        self.inicia_pontos()
        
    def inicia_pontos(self):
        pontos_string = 'Pontos: ' + str(self.estado_jogo.pontos)
        self.pontos_imagem = self.fonte.render(pontos_string, True, self.cor_texto)
        
        self.score_rect = self.pontos_imagem.get_rect()
        self.score_rect.left = 20
        self.score_rect.top = 20

        """Mostra o nivel atual."""

        nivel_string = 'Nivel: ' + str(self.estado_jogo.nivel)
        self.nivel_imagem = self.fonte.render(nivel_string, True, self.cor_texto)

        self.nivel_rect = self.nivel_imagem.get_rect()
        self.nivel_rect.left = 20
        self.nivel_rect.top = self.score_rect.top + 50
        
    def mostra_pontos(self):
        """ Desenha pontos na tela"""
        self.screen.blit(self.pontos_imagem, self.score_rect)
        self.screen.blit(self.nivel_imagem, self.nivel_rect)