class Ranking():
    def __init__(self, bd_score, nome_player):
        self.ranking = open(bd_score, '+a')
        self.pontos_ordenados = None
        self.nome_player = nome_player

    def add_score(self, pontos):
        if pontos > 0:
            rank = self.get_ranking()
            if len(rank) < 10:
                self.ranking.write(self.nome_player + "\n")
                self.ranking.write(str(pontos) + "\n")
            elif pontos >= self.pontos_ordenados[-1]:
                self.add_score_tupla({1: 'ok', 0: 'lol'}) #<------# p/ organizar

    def get_ranking(self):
        rank = {}
        self.ranking.close()
        self.ranking = open('bd_score', 'r')
        i = 0
        linhas = self.ranking.readlines()
        while i < len(linhas) -1:
            nome = linhas[i]
            nome = nome.split('\n')[0]
            rank.update({int(linhas[i+1]):nome})
            i += 2
        self.ranking = open('bd_score', '+a')
        self.pontos_ordenados = sorted(rank, reverse=True)
        rank_tmp = {}
        for i in self.pontos_ordenados:
            rank_tmp.update({i:rank[i]})
        return rank_tmp

    def add_score_tupla(self, tupla):
        # print(tupla)
        pass
