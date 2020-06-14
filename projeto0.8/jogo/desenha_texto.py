import pygame

def texto(screen, texto, posicao, cor, tamanho_fonte):
    fonte = pygame.font.SysFont(None, tamanho_fonte)
    string_imagem = fonte.render(texto, True, cor)

    rect = string_imagem.get_rect()
    rect.center = posicao
    screen.blit(string_imagem, rect)