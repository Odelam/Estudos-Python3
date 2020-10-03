def jogar_forca():
    print("*" * 20)
    print("Jogo da forca!")
    print("*" * 20)

    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    enforcou = False
    acertou = False

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = str(input("Qual letra? ")).strip().upper()

        index = 0
        for letra in palavra_secreta:
            if chute == letra.upper():
                letras_acertadas[index] = letra
            index += 1
        print(letras_acertadas)
        print("Jogando")

    print("Fim do jogo!")


if __name__ == '__main__':
    jogar_forca()
