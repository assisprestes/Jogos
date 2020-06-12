import sys
from xo_doenca import Jogo
#from teste import Teste


jogo = None
tela_teste = None

def inicia_jogo():
    nome_player = ''
    if sys.argv.__len__() < 2:
        print('\n+========================================')
        nome_player = input('| Digite seu nome player: ')
        print('+========================================')
    else:
        nome_player = sys.argv[1]
    jogo = Jogo(nome_player)
    jogo.resetar()
    jogo.run_game()


def resetar_jogo():

    inicia_jogo()


def main():
    inicia_jogo()
    # tela_teste = Teste()
    # tela_teste.run_game()


if __name__ == '__main__':
    main()
