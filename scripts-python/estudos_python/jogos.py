import adivinha_jogo
import forca_jogo


def escolhe_jogo():
    print("*" * 31)
    print(("=" * 5), "Escolha o seu jogo!", ("=" * 5))
    print("*" * 31)

    print('''
    [1] - Forca;
    [2] - Adivinhação;
    ''')
    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("Jogando Forca")
        forca_jogo.jogar_forca()
    elif jogo == 2:
        print("Jogando Adivinhação")
        adivinha_jogo.jogar_adivinhacao()


if __name__ == '__main__':
    escolhe_jogo()
