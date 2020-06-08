import pygame
from pygame.sprite import Group

import game_functions as gf
from atualiza_movimento import UpMovBarra
from atualiza_movimento import UpMovVirus
from barra_tempo import Barra_tempo
from botao import Botao
from estado_jogo import EstadoJogo
from mira import Mira
from mira_colisor import Mira_colisor
from painel_vacina import Painel_vacina
from pontuacao import Pontuacao
from ranking import Ranking
from settings import Settings

class Jogo():

    def resetar(self):

        pygame.init()
        self.ai_settings = Settings()

        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))
        # ponteiro do mause disaparece
        pygame.mouse.set_visible(True)
        # Cria espaçonave
        self.painel_vacina = Painel_vacina(self.ai_settings, self.screen)
        self.mira = Mira(self.ai_settings, self.screen, self.painel_vacina)
        # Grupo de virus
        self.viroses = Group()
        self.miras = Group()
        self.mira_colisor = Mira_colisor(self.ai_settings, self.screen)
        self.miras.add(self.mira_colisor)

        pygame.display.set_caption('Xo doenca.')
        # Define background
        self.background = pygame.image.load(self.ai_settings.background_path)
        self.background = pygame.transform.scale(self.background, (self.ai_settings.screen_width, self.ai_settings.screen_height))
        """ Define o estado do jogo"""

        self.barra_tempo = Barra_tempo(self.ai_settings, self.screen)

        self.estado_jogo = EstadoJogo(self.ai_settings, self.viroses, self.screen, self.painel_vacina, self.barra_tempo)
        if self.estado_jogo.fullscreen:
            self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height), pygame.FULLSCREEN)

        self.pontuacao_placar = Pontuacao(self.ai_settings, self.screen, self.estado_jogo)
        self.pontuacao_placar.inicia_pontos()

        self.estado_jogo.pontuacao = self.pontuacao_placar

        grupos_viroses = gf.coloca_virus_tela(self.ai_settings, self.screen, self.viroses, self.estado_jogo)

        self.estado_jogo.set_grupo_viroses(grupos_viroses)

        """ Indica estado do jogo se está iniciado ou não"""

        # Define um multiprocess
        self.atualiza_movimento = UpMovVirus(self.viroses)

        self.atualiza_barra_tempo = UpMovBarra(self.barra_tempo)

        self.ranking_bd = Ranking('bd_score')

        self.play_botao = Botao(self.ai_settings, self.screen, './imagens/icones/iniciar.png')
        self.ranking_botao = Botao(self.ai_settings, self.screen, './imagens/icones/ranking.png')
        self.play_botao.rect.centerx = 350
        self.play_botao.rect.bottomleft = (self.screen.get_rect().bottomleft[0] + 50, self.screen.get_rect().bottomleft[1] - 50)
        self.ranking_botao.rect.bottomright = (self.screen.get_rect().bottomright[0] - 50, self.screen.get_rect().bottomright[1] - 50)



    def run_game(self):
        
        # estado_jogo.jogo_estado = False
        while True:
            gf.check_events(self.ai_settings, self.screen,self.mira, self.mira_colisor, self.painel_vacina, self.miras, self.viroses,
                            self.estado_jogo.grupo_viroses, self.estado_jogo, self.pontuacao_placar, self.barra_tempo, self.play_botao,
                            self.atualiza_movimento, self.atualiza_barra_tempo, self.ranking_botao, self.ranking_bd)
            if self.estado_jogo.jogo_estado:
                gf.update_screen(self.ai_settings, self.screen, self.mira, self.painel_vacina, self.viroses, self.miras, self.background, self.pontuacao_placar,
                                 self.barra_tempo, self.play_botao)
                # Percorre os update atacado no modulo principal
                gf.update_logica(self.ai_settings, self.viroses, self.painel_vacina, self.barra_tempo, self.mira, self.estado_jogo, self.ranking_bd)
                # Desenha o botão Play se o jogo estiver inativo
                
            if not self.estado_jogo.jogo_estado:
               # Tela recente fica visivel
                pygame.mouse.set_visible(True)
            else:
                pygame.mouse.set_visible(False)

            if not self.estado_jogo.jogo_estado and not self.ranking_botao.flag_click:
                self.resetar()
                self.screen.fill((200, 100, 100), self.screen.get_rect())
                self.screen.blit(self.background, self.background.get_rect())
                self.play_botao.draw_botao()
                self.ranking_botao.draw_botao()
            if not self.estado_jogo.jogo_estado and self.ranking_botao.flag_click:
                self.play_botao.draw_botao()
                self.ranking_botao.draw_botao()
            gf.is_fim_jogo(self.barra_tempo, self.estado_jogo, self.ranking_bd, self.screen)
            pygame.display.flip()

