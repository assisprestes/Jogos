class Ranking():
    def __init__(self, bd_score, nome_player):
        self.bd_score = bd_score
        self.ranking = open(self.bd_score, '+a')
        self.pontos_ordenados = None
        self.nome_player = nome_player

    def abre_arquivo_w(self):
        self.ranking = open(self.bd_score, 'w')

    def menor_score(self):
        self.abre_ranking_read()
        try:
            return sorted(self.get_ranking())[0]
        except:
            return 0

    def abre_ranking_read(self):
        self.ranking.close()
        self.ranking = open('bd_score', 'r')

    def fecha_ranking(self):
        self.ranking.close()

    # Garantir que a quantidade de scores no arquivo seja menor ou  igual a 10
    # Qual é o menor ponto
    # verica
    # pontos recebido maior ou igual a ponto minimo
    # coloca no arquivo

    def add_score(self, pontos):
        menor_pontos = self.menor_score()
        if pontos > 0:
            rank = self.get_ranking()
            if pontos >= menor_pontos or len(rank) < 10:
                rank.update({pontos: self.nome_player})
                self.abre_arquivo_w()
                j = -1
                for i in rank:
                    j += 1
                    if j == 10:
                        break
                    self.ranking.write(rank[i] + "\n")
                    self.ranking.write(str(i) + "\n")

    def get_ranking(self):
        rank = {}
        self.abre_ranking_read()
        i = 0
        linhas = self.ranking.readlines()
        while i < len(linhas) -1:
            nome = linhas[i]
            nome = nome.split('\n')[0]
            rank.update({int(linhas[i+1]):nome})
            i += 2
        self.fecha_ranking()
        self.ranking = open('bd_score', '+a')
        self.pontos_ordenados = sorted(rank, reverse=True)
        rank_tmp = {}
        for i in self.pontos_ordenados:
            rank_tmp.update({i:rank[i]})
        return rank_tmp

    def persiste_score(self,scores):

        pass
