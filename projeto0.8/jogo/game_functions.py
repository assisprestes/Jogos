import sys
import pygame
import time

from atualiza_movimento import UpMovVirus
from painel_vacina import Painel_vacina
from virus import Virus
from random import randint
from pygame.sprite import Group
from pygame.sprite import groupcollide
import desenha_texto


def check_colision_virus1(miras, viroses, estado_jogo, pontuacao_placar, ai_settings, barra_tempo):
    colidir = groupcollide(miras, viroses, False, True)
    if colidir:
        estado_jogo.pontos += (ai_settings.fator_base_pontos * ai_settings.speed1)
        if barra_tempo.tamanho_barra + 50 < barra_tempo.tamanho_maximo:
            barra_tempo.tamanho_barra += 50
        elif barra_tempo.tamanho_barra + 50 > barra_tempo.tamanho_maximo:
            barra_tempo.tamanho_barra = barra_tempo.tamanho_maximo


def check_colision_virus2(miras, viroses, estado_jogo, pontuacao_placar, ai_settings, barra_tempo):
    colidir = groupcollide(miras, viroses, False, True)
    if colidir:
        estado_jogo.pontos += (ai_settings.fator_base_pontos * ai_settings.speed2)
        if barra_tempo.tamanho_barra + 50 < barra_tempo.tamanho_maximo:
            barra_tempo.tamanho_barra += 50
        elif barra_tempo.tamanho_barra + 50 > barra_tempo.tamanho_maximo:
            barra_tempo.tamanho_barra = barra_tempo.tamanho_maximo


def check_colision_virus3(miras, viroses, estado_jogo, pontuacao_placar, ai_settings, barra_tempo):
    colidir = groupcollide(miras, viroses, False, True)
    if colidir:
        estado_jogo.pontos += (ai_settings.fator_base_pontos * ai_settings.speed3)
        if barra_tempo.tamanho_barra + 50 < barra_tempo.tamanho_maximo:
            barra_tempo.tamanho_barra += 50
        elif barra_tempo.tamanho_barra + 50 > barra_tempo.tamanho_maximo:
            barra_tempo.tamanho_barra = barra_tempo.tamanho_maximo


def check_colision_virus4(miras, viroses, estado_jogo, pontuacao_placar, ai_settings, barra_tempo):
    colidir = groupcollide(miras, viroses, False, True)
    if colidir:
        estado_jogo.pontos += (ai_settings.fator_base_pontos * ai_settings.speed4)
        if barra_tempo.tamanho_barra + 50 < barra_tempo.tamanho_maximo:
            barra_tempo.tamanho_barra += 50
        elif barra_tempo.tamanho_barra + 50 > barra_tempo.tamanho_maximo:
            barra_tempo.tamanho_barra = barra_tempo.tamanho_maximo


# Coloca os virus na tela.
def coloca_virus_tela(ai_settings, screen, viroses, estado_jogo):
    grupo_virus1 = Group()
    grupo_virus2 = Group()
    grupo_virus3 = Group()
    grupo_virus4 = Group()

    for i in range(0, 5):
        virus1 = gerar_virus(ai_settings, screen, "virus1", estado_jogo)  # Virus azul
        virus1.update_direcao(0, 7)
        grupo_virus1.add(virus1)
        viroses.add(grupo_virus1)

    for i in range(0, 5):
        virus2 = gerar_virus(ai_settings, screen, "virus2", estado_jogo)
        virus2.update_direcao(0, 7)
        grupo_virus2.add(virus2)
        viroses.add(grupo_virus2)

    for i in range(0, 5):
        virus3 = gerar_virus(ai_settings, screen, "virus3", estado_jogo)  # Virus marrom
        virus3.update_direcao(0, 7)
        grupo_virus3.add(virus3)
        viroses.add(grupo_virus3)

    for i in range(0, 5):
        virus4 = gerar_virus(ai_settings, screen, "virus4", estado_jogo)  # Virus verde
        virus4.update_direcao(0, 7)
        grupo_virus4.add(virus4)
        viroses.add(grupo_virus4)

    return (grupo_virus1, grupo_virus2, grupo_virus3, grupo_virus4)


# cria um virus em uma posiçao aleatoria da tela;
def gerar_virus(ai_settings, screen, tipo_virus, estado_jogo):
    virus_tmp = Virus(ai_settings, screen, tipo_virus, estado_jogo)
    virus_tmp.rect.bottomright = (
        randint(virus_tmp.largura, ai_settings.screen_width), randint(virus_tmp.altura, ai_settings.screen_height))
    return virus_tmp


def check_keydown_events(event, ai_settings, screen, mira):
    """Responde ao mouse"""
    if event.key == pygame.K_RIGHT:
        mira.moving_rigth = True
    elif event.key == pygame.K_LEFT:
        mira.moving_left = True
    elif event.key == pygame.K_SPACE:
        pass
    # Comando de interface do usuário
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, ship):
    # solicitação de tecla solta
    if event.key == pygame.K_RIGHT:
        ship.moving_rigth = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


# Verifica evento relacionados ao movimento do mause
def checar_mouse_motion(event, mira, mira_colisor):
    mira.rect.centerx = event.pos[0]
    mira.rect.centery = event.pos[1]
    mira_colisor.rect.centerx = event.pos[0]
    mira_colisor.rect.centery = event.pos[1]


def checar_mouse_botao(event, painel_vacina, miras, viroses, grupo_virose, estado_jogo, pontuacao_placar, ai_settings,
                       barra_tempo, sons):
    if not estado_jogo.pause:# Verifica se roleta  foi posicionado para cima
        if event.button == pygame.MOUSEBUTTONDOWN or event.button == 3:
            painel_vacina.vacina_selecionada += 1
            sons.troca_vacinas.play()
        elif event.button == pygame.MOUSEMOTION:
            painel_vacina.vacina_selecionada -= 1
            sons.troca_vacinas.play()
        elif event.button == pygame.BUTTON_LEFT:
            sons.click.play()
            if painel_vacina.vacina_selecionada == painel_vacina.vacinas.index('vacina1'):
                check_colision_virus1(miras, grupo_virose[painel_vacina.vacinas.index('vacina1') - 1], estado_jogo,
                                  pontuacao_placar, ai_settings, barra_tempo)
            elif painel_vacina.vacina_selecionada == painel_vacina.vacinas.index('vacina2'):
                check_colision_virus2(miras, grupo_virose[painel_vacina.vacinas.index('vacina2') - 1], estado_jogo,
                                  pontuacao_placar, ai_settings, barra_tempo)
            elif painel_vacina.vacina_selecionada == painel_vacina.vacinas.index('vacina3'):
                check_colision_virus3(miras, grupo_virose[painel_vacina.vacinas.index('vacina3') - 1], estado_jogo,
                                  pontuacao_placar, ai_settings, barra_tempo)
            elif painel_vacina.vacina_selecionada == painel_vacina.vacinas.index('vacina4'):
                check_colision_virus4(miras, grupo_virose[painel_vacina.vacinas.index('vacina4') - 1], estado_jogo,
                                  pontuacao_placar, ai_settings, barra_tempo)
        pontuacao_placar.inicia_pontos()
        painel_vacina.vacina_selecionada %= 4



def check_events(ai_settings, screen, mira, mira_colisor, painel_vacina, miras, viroses, grupos_viroses, estado_jogo,
                 pontuacao_placar, barra_tempo, play_botao,
                 atualiza_movimento, atualiza_barra_tempo, ranking_botao, ranking_bd, sons, vetor_botoes):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, mira)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mira)
        elif event.type == pygame.MOUSEMOTION:
            checar_mouse_motion(event, mira, mira_colisor)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            checar_mouse_botao(event, painel_vacina, miras, viroses, grupos_viroses, estado_jogo, pontuacao_placar,
                               ai_settings, barra_tempo, sons)
            # Verifica se iniciar foi clicado
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_buttons(estado_jogo, play_botao, mouse_x, mouse_y, atualiza_movimento, atualiza_barra_tempo,
                          ranking_botao, ranking_bd, screen, viroses, barra_tempo, ai_settings, vetor_botoes)


def update_screen(ai_settings, screen, mira, painel_vacina, viroses, miras, background, pontuacao_placar, barra_tempo,
                  play_botao, ranking_botao, ranking_bd, pause_botao):

    """Atualiza imagen na tela"""
    screen.fill(ai_settings.bg_color)
    if ai_settings.background_visivel:
        screen.blit(background, background.get_rect())
    # desenha virus na tela
    for virus in viroses.sprites():
        virus.draw_virus()
    for virus in miras.sprites():
        virus.draw_mira()
    barra_tempo.desenha_barra(screen)
    pontuacao_placar.mostra_pontos()
    pause_botao.draw_botao()
    mira.blitme()
    painel_vacina.desenha_painel_vacina(ai_settings, screen)

    if play_botao.is_visivel:
        play_botao.draw_botao()

    if ranking_botao.is_visivel:
        ranking_botao.draw_botao()
    # play_botao.draw_botao()


def update_viroses(viroses):
    """Atualiza vírus."""
    viroses.update()


def update_logica(ai_settings, viroses, painel_vacina, barra_tempo, mira, estado_jogo, ranking_bd):
    estado_jogo.next_nivel()
    mira.update()
    update_viroses(viroses)
    painel_vacina.update(ai_settings)


def mostra_tela_game_over(screen, estado_jogo, play_botao, ranking_botao):
    pygame.mouse.set_visible(True)
    play_botao.is_visivel = True
    screen.fill((200, 100, 100), screen.get_rect())
    play_botao.ativo = True
    ranking_botao.ativo = True
    ranking_botao.is_visivel = True
    if play_botao.is_visivel:
        play_botao.draw_botao()
    if ranking_botao.is_visivel:
        ranking_botao.draw_botao()
    centery = screen.get_rect().centery - 80
    desenha_texto.texto(screen, "FIM DE JOGO", (screen.get_rect().centerx, centery), (255, 0, 0), 100)
    desenha_texto.texto(screen, "pontos: " + str(estado_jogo.pontos), (screen.get_rect().centerx, centery + 100),
                        (0, 0, 0), 60)


def is_fim_jogo(barra_tempo, estado_jogo, ranking_bd, screen, play_botao, ranking_botao):
    if barra_tempo.barra_vazia:
        barra_tempo.barra_vazia = False
        if estado_jogo.jogo_estado:
            mostra_tela_game_over(screen, estado_jogo, play_botao, ranking_botao)
            pygame.display.flip()
            ranking_bd.add_score( estado_jogo.pontos)  # <-----------
            # Exibe a pontuação por 5 segundos
            time.sleep(5)
        estado_jogo.jogo_estado = False
        # ranking_tela(ranking_bd, screen)
        # sys.exit()


# Tela de ranking

def ranking_tela(ranking_bd, screen, ai_settings, play_botao, ranking_botao):
    screen.fill((40, 40, 40), screen.get_rect())
    background = pygame.image.load('imagens/background/ranking_tela.jpg')
    rect = pygame.Rect(0 , 0, ai_settings.screen_width, ai_settings.screen_height  )#Inconsistencia
    rect.centerx = 650#int(screen.get_rect()[2]/2)
    screen.blit(background, rect)
    rank = ranking_bd.get_ranking()
    desenha_texto.texto(screen, "Ranking", (screen.get_rect().centerx, 60), (0, 255, 0), 100)

    play_botao.draw_botao()
    ranking_botao.draw_botao()
    i = 1
    for posicao in rank:
        if i > 8:
            break
        desenha_texto.texto(screen, str(i) + ": " + str(posicao) + "   " + rank[posicao],
                            (screen.get_rect().centerx, (i * 50) + 120), (0, 0, 0), 50)
        i += 1
    pygame.display.flip()


def check_buttons(estado_jogo, play_botao, mouse_x, mouse_y, atualiza_movimento, atualiza_barra_tempo,
                  ranking_botao, ranking_bd, screen, viroses, barra_tempo, ai_settings, vetor_botoes):
    for botao in vetor_botoes:
        if botao.rect.collidepoint(mouse_x, mouse_y) and botao.ativo:
            botao.funcao_call_back()



def reseta_jogo(barra_tempo, estado_jogo):
    barra_tempo.tamanho_barra = barra_tempo.tamanho_maximo
    estado_jogo.jogo_estado = True
