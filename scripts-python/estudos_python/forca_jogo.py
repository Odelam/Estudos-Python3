import random


def jogar_forca():
    imprime_msg_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while not enforcou and not acertou:
        chute = solicita_chute_usuario()

        if chute in palavra_secreta:
            guarda_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            tentativas += 1

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_msg_vencedor()
    else:
        imprime_msg_perdedor()


def imprime_msg_abertura():
    print("*" * 20)
    print("Jogo da forca!")
    print("*" * 20)


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    lista_palavra = []

    for linha in arquivo:
        linha = linha.strip()
        lista_palavra.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(lista_palavra))
    palavra_secreta = lista_palavra[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]  # modo pythônico de se fazer
    # for letra in palavra_secreta:
    #     letras_acertadas.append("_")


def solicita_chute_usuario():
    return str(input("Qual letra? ")).strip().upper()


def guarda_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def imprime_msg_vencedor():
    print("Você venceu!")
    print()


def imprime_msg_perdedor():
    print("Você perdeu!")
    print()


if __name__ == '__main__':
    jogar_forca()
