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

    def __init__(self, barra_tempo):
        Thread.__init__(self)
        self.janela_ativa = True
        self.daemon = True
        self.barra_tempo = barra_tempo

    def run(self) -> None:
        while self.janela_ativa:
            sleep(self.barra_tempo.fator_decressimo)
            self.barra_tempo.atualiza_barra()