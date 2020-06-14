from pygame.threads import Thread
from time import sleep

class UpMovVirus(Thread):

    def __init__(self, viroses):
        Thread.__init__(self)
        self.janela_ativa = True
        self.daemon = True
        self.viroses = viroses

    def run(self) -> None:
        while True:
            sleep(.02)
            for virus in self.viroses:
                virus.mover()


class UpMovBarra(Thread):

    def __init__(self, barra_tempo, viroses):
        Thread.__init__(self)
        self.viroses = viroses
        self.janela_ativa = True
        self.daemon = True
        self.barra_tempo = barra_tempo
        self.ativo = True

    def run(self) -> None:
        while self.janela_ativa:
            sleep(self.barra_tempo.fator_decressimo)
            if self.ativo:
                self.barra_tempo.atualiza_barra()
            # self.barra_tempo.tamanho_barra = self.barra_tempo.tamanho_maximo
