import random


def jogar_adivinhacao():
    print("*" * 20)
    print("Jogo de adivinhação!")
    print("*" * 20)

    numero_secreto = random.randrange(1, 101)  # vai de 1 a 100
    total_tentativas = 0
    pontos = 100

    print("número secreto", numero_secreto)
    print("Qual nível de dificuldade?")
    print('''
    [1] - Fácil;
    [2] - Médio;
    [3] - Difícil;''')
    nivel = int(input("Escolha qual nível: "))
    print()

    while nivel > 3:
        print("Nível fora do range!")
        print()
        print("Qual nível de dificuldade?")
        print('''
            [1] - Fácil;
            [2] - Médio;
            [3] - Difícil;''')
        nivel = int(input("Escolha qual nível: "))
        print()

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print(f"Tentativa {rodada} de {total_tentativas}.")
        chute = int(input("Digite um número entre 1 e 100: "))
        print(f"Você digitou: {chute}")
        print()

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f"Você acertou e fez {pontos} pontos!")
            print()
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior do que o número secreto.")
                print()
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto.")
                print()
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do jogo!")


if __name__ == '__main__':
    jogar_adivinhacao()
