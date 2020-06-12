import pygame


class Sons:
    def __init__(self):
        pygame.mixer.init()
        self.click = pygame.mixer.Sound('./audios/click.wav')
        self.troca_vacinas = pygame.mixer.Sound('./audios/troca_vacina.wav')
        self.troca_vacinas.set_volume(.2)
