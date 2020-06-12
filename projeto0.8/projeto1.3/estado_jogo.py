import game_functions as gf

class EstadoJogo():

    def __init__(self, ai_settings, viroses, screen, painel_vacina, barra_tempo, atualiza_movimento):
        self.atualiza_movimento = atualiza_movimento
        self.ai_settings = ai_settings
        self.pontos = 0
        self.fullscreen = False
        self.nivel = 1
        self.viroses = viroses
        self.screen = screen
        self.painel_vacina =painel_vacina
        self.grupo_viroses = None
        self.barra_tempo = barra_tempo
        self.pontuacao = None
        self.jogo_estado = False

    def set_grupo_viroses(self,grupo_viroses):
        self.grupo_viroses = grupo_viroses

    def estado_reset(self):
        self.pontos = 0

    def next_nivel(self):
        if not self.viroses.__len__():
            self.barra_tempo.tamanho_barra = self.barra_tempo.tamanho_maximo
            self.nivel += 1
            for virus in self.viroses:
                if virus.tipo == "virus1":
                    virus.speed = self.ai_settings.speed1 * self.nivel
                elif virus.tipo == "virus2":
                    virus.speed = self.ai_settings.speed2 * self.nivel
                elif virus.tipo == "virus3":
                    virus.speed = self.ai_settings.speed3 * self.nivel
                elif virus.tipo == "virus4":
                    virus.speed = self.ai_settings.speed4 * self.nivel

            self.barra_tempo.barra_vazia = False
            self.grupo_viroses = gf.coloca_virus_tela(ai_settings=self.ai_settings, viroses=self.viroses, estado_jogo=self, screen=self.screen)
            self.painel_vacina.vacina_selecionada = 0
            self.barra_tempo.redefine_barra_tempo()
            self.pontuacao.inicia_pontos()
