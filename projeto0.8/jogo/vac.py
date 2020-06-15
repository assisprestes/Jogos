import pygame
from pygame.sprite import Group
from time import sleep

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
from sons import Sons


class Jogo():


    def __init__(self, nome_player):
        pygame.mixer.init()
        pygame.mixer.music.load('./audios/menu.wav')
        self.nome_player = nome_player
        self.ranking_botao_clicado = False

    def resetar(self):

        pygame.init()

        self.sons = Sons()

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

        pygame.display.set_caption('VAC')
        # Define background
        self.background = pygame.image.load(self.ai_settings.background_path)
        self.background = pygame.transform.scale(self.background, (self.ai_settings.screen_width + 500, self.ai_settings.screen_height))

        self.background_init = pygame.image.load(self.ai_settings.background_path_init)
        self.background_init = pygame.transform.scale(self.background_init, (self.ai_settings.screen_width, self.ai_settings.screen_height))
        """ Define o estado do jogo"""

        self.barra_tempo = Barra_tempo(self.ai_settings, self.screen)
        # Define um multiprocess
        self.atualiza_movimento = UpMovVirus(self.viroses)
        self.estado_jogo = EstadoJogo(self.ai_settings, self.viroses, self.screen, self.painel_vacina, self.barra_tempo, self.atualiza_movimento)
        self.barra_tempo.estado_jogo = self.estado_jogo
        if self.estado_jogo.fullscreen:
            self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height), pygame.FULLSCREEN)

        self.pontuacao_placar = Pontuacao(self.ai_settings, self.screen, self.estado_jogo)
        self.pontuacao_placar.inicia_pontos()

        self.estado_jogo.pontuacao = self.pontuacao_placar

        grupos_viroses = gf.coloca_virus_tela(self.ai_settings, self.screen, self.viroses, self.estado_jogo)

        self.estado_jogo.set_grupo_viroses(grupos_viroses)

        """ Indica estado do jogo se está iniciado ou não"""

        # Define um multiprocess

        self.atualiza_barra_tempo = UpMovBarra(self.barra_tempo, grupos_viroses)

        self.ranking_bd = Ranking('bd_score', self.nome_player)

        self.play_botao = Botao(self.ai_settings, self.screen, './imagens/icones/iniciar.png', self.func_call_back_play)
        self.ranking_botao = Botao(self.ai_settings, self.screen, './imagens/icones/ranking.png', self.func_call_back_ranking)
        self.play_botao.rect.centerx = 350
        self.play_botao.rect.bottomleft = (self.screen.get_rect().bottomleft[0] + 50, self.screen.get_rect().bottomleft[1] - 50)
        self.ranking_botao.rect.bottomright = (self.screen.get_rect().bottomright[0] - 50, self.screen.get_rect().bottomright[1] - 50)


        self.pause_botao = Botao(self.ai_settings, self.screen, './imagens/icones/pause-play.png', self.func_call_back_pause)
        self.pause_botao.altura = 50
        self.pause_botao.largura = 50
        self.pause_botao.make_rect()
        self.pause_botao.rect.centerx = self.ai_settings.screen_width - 30
        self.pause_botao.rect.centery = 70

        self.vetor_botoes = []
        self.vetor_botoes.append(self.play_botao)
        self.vetor_botoes.append(self.ranking_botao)
        self.vetor_botoes.append(self.pause_botao)

        pygame.mixer.music.play(-1)

    """Inicia um novo jogo quando o jogador clicar em Play."""
    def func_call_back_play(self):
        print('CARREGANDO JOGO ...')
        if not self.estado_jogo.jogo_estado:
            try:
                self.resetar()
                self.atualiza_movimento.start()
                self.atualiza_barra_tempo.start()
            except:
                self.atualiza_movimento = UpMovVirus(self.viroses)
                self.atualiza_barra_tempo = UpMovVirus(self.viroses)
                gf.reseta_jogo(self.barra_tempo, self.estado_jogo)
        self.estado_jogo.jogo_estado = True
        self.play_botao.ativo = False
        self.ranking_botao.ativo = False
        self.play_botao.is_visivel = False
        self.ranking_botao.is_visivel = False

    def func_call_back_pause(self):
        self.estado_jogo.pause = not self.estado_jogo.pause

    """Inicia um novo jogo quando o jogador clicar em Play."""
    def func_call_back_ranking(self):
        self.ranking_botao.flag_click = True
        gf.ranking_tela(self.ranking_bd, self.screen, self.ai_settings, self.play_botao, self.ranking_botao)

    def funcao_desenha(self):
        gf.update_screen(self.ai_settings, self.screen, self.mira, self.painel_vacina, self.viroses, self.miras, self.background, self.pontuacao_placar,
                            self.barra_tempo, self.play_botao, self.ranking_botao, self.ranking_bd, self.pause_botao)
        # Percorre os update atacado no modulo principal
        gf.update_logica(self.ai_settings, self.viroses, self.painel_vacina, self.barra_tempo, self.mira, self.estado_jogo, self.ranking_bd)
        # Desenha o botão Play se o jogo estiver inativo
        pygame.display.flip()

    def tela_inicial(self):
        if not self.estado_jogo.jogo_estado:
            self.screen.fill((200, 100, 100), self.screen.get_rect())
            self.screen.blit(self.background_init, self.background_init.get_rect())
            self.play_botao.draw_botao()
            self.ranking_botao.draw_botao()
        if not self.ranking_botao_clicado:
            pygame.display.flip()

    def run_game(self):
        print('Jogo iniciado ...')
        self.tela_inicial()
        # estado_jogo.jogo_estado = False
        while True:

            gf.check_events(self.ai_settings, self.screen,self.mira, self.mira_colisor, self.painel_vacina, self.miras, self.viroses,
                            self.estado_jogo.grupo_viroses, self.estado_jogo, self.pontuacao_placar, self.barra_tempo, self.play_botao,
                            self.atualiza_movimento, self.atualiza_barra_tempo, self.ranking_botao, self.ranking_bd, self.sons, self.vetor_botoes)


            if self.ranking_botao.flag_click:
                self.ranking_botao.flag_click = False
                # ranking_tela(ranking_bd,screen, ai_settings, play_botao, ranking_botao)
                gf.ranking_tela(self.ranking_bd, self.screen, self.ai_settings, self.play_botao, self.ranking_botao)
                self.ranking_botao_clicado = True

            if self.estado_jogo.jogo_estado:
                self.funcao_desenha()

            if not self.estado_jogo.jogo_estado:
               # Tela recente fica visivel
                pygame.mouse.set_visible(True)
            else:
                pygame.mouse.set_visible(False)

            self.tela_inicial()

            gf.is_fim_jogo(self.barra_tempo, self.estado_jogo, self.ranking_bd, self.screen, self.play_botao, self.ranking_botao)

