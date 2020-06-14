import pygame.font
class Botao():
    def __init__(self, ai_settings, screen, msg, funcao_call_back):
        self.msg = msg
        self.ativo = True
        self.is_visivel = True
        self.funcao_call_back = funcao_call_back
        """Inicializa os atributos do botão."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
    # Define as dimensões e as propriedades do botão,
        self.largura, self.altura = 150, 150
    # Constrói o objeto rect do botão e o centraliza
        self.make_rect()
        self.botao_rect = self.botao.get_rect()
        self.botao_rect.center = self.rect.center
        # self.msg_image = #self.font.render(msg, True, self.text_color, self.button_color)
        self.rect.centery = self.screen.get_rect().centery
        self.flag_click = False

    def make_rect(self):
    # A mensagem do botão deve ser preparada apenas uma vez
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.botao = pygame.image.load(self.msg)
        self.botao = pygame.transform.scale(self.botao, (self.largura, self.altura))

    def draw_botao(self):  # Desenha um botão em branco e, em seguida, desenha a mensagem
        # self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.botao, self.rect)