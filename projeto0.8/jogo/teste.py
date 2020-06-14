import pygame
from sys import exit
from animacao import Animacao
from virus import Virus


class Teste:


    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('TESTES')


    def run_game(self):
        animacao = Animacao('./imagens/virus/Virus03', self.screen , 100, 100);
        animacao.rect.center = animacao.rect_screen.center
        animacao.visivel = True
        while True:
            self.check_events()
            self.screen.fill((50, 50, 50), self.screen.get_rect())
            animacao.update()
            pygame.display.flip()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


from ranking import Ranking

class Teste_ranking:
    def __init__(self, ranking):
        self.ranking = ranking

    def run_teste(self):
        print('Teste 8 iniciado ...')
        print('Menor pontos do ranking: ', self.ranking.menor_score())
        for i in range(0, 15):
            self.ranking.add_score(8000 + i)
        print('Novo menor pontos do ranking: ', self.ranking.menor_score())
        print(self.ranking.get_ranking())


teste_ranking = Teste_ranking(Ranking('bd_score', 'Tests'))
teste_ranking.run_teste()