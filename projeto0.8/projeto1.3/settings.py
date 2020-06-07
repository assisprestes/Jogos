class Settings:
    def __init__(self):
        """Classe para armazenar configuraçõesa"""
        self.screen_width = 1024
        self.screen_height = 600
        self.bg_color = (255, 60, 60)
        """configuração da mira"""
        self.mira_tamanho = (300, 300)

        """Configuração Painel"""

        self.painel_vacina_cor = (0,0,0)
        self.painel_largura = 280
        self.painel_altura = 140
        self.painel_largura_borda = 3
        self.painel_dist_borda = 30
        self.painel_vacina_padrao = 0
        self.painel_tamanho_vacina = (120, 120)
        self.painel_fator_selecao = 50
        
        """Configuraçoes de tela de fundo"""
        
        self.background_path ='imagens/background/30145.jpg'
        self.background_visivel = False
        
        """Configurações globais"""
        
        self.pontos_virus1_acerto = 50
        
        """ Vírus fator velocidade"""
        
        self.fator_base_pontos = 50
        
        
        self.speed1 = 2 # Fator do vírus azul
        self.speed2 = 1 # Fator do vírus amarelo
        self.speed3 = 3 # Fator vírus marrom
        self.speed4 = 2 # Fator do vírus verde