from vac import Jogo


jogo = Jogo()


def inicia_jogo():
    jogo.resetar()
    jogo.run_game()


def resetar_jogo():
    inicia_jogo()


def main():
    inicia_jogo()


if __name__ == '__main__':
    main()
