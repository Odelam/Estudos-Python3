import random, sys

vitorias = derrotas = empates = 0

while True: # loop principal do jogo
    while True: # loop de entrada do jogador
        print(f"'{vitorias} Vitórias, '{derrotas} Derrotas, '{empates}' Empates.")
        jogada = str(input("[P]edra, [PP}apel, [T]esoura ou [S]air: ")).strip().upper()
        if jogada == 'S':
            sys.exit() # sai do programa
        if jogada == 'P' or jogada == 'PP' or jogada == 'T':
            if jogada == 'P':
                print('PEDRA vs ....')
            elif jogada == 'PP':
                print("PAPEL vs...")
            elif jogada == 'T':
                print("TESOURA vs...")

            # mostra o caminho que o pc escolheu
            aleatorio_num = random.randint(1, 3)
            if aleatorio_num == 1:
                jogada_maquina = 'P'
                print("PEDRA.")
            elif aleatorio_num == 2:
                jogada_maquina = 'PP'
                print("PAPEL.")
            elif aleatorio_num == 3:
                jogada_maquina = 'T'
                print("TESOURA.")

            # registrar e mostrar derrota/vitoria/empate
            if jogada == jogada_maquina:
                print('É um empate!')
                empates += 1
            elif jogada == 'P' and jogada_maquina == 'T':
                print("Você ganhou!")
                vitorias += 1
            elif jogada == 'PP' and jogada_maquina == 'P':
                print("Você venceu!")
                vitorias += 1
            elif jogada == 'T' and jogada_maquina == 'PP':
                print("Você venceu!")
                vitorias += 1
            elif jogada == 'P' and jogada_maquina == 'PP':
                print("Você perdeu!")
                derrotas += 1
            elif jogada == 'PP' and jogada_maquina == 'T':
                print("Você perdeu!")
                derrotas += 1
            elif jogada == 'T' and jogada_maquina == 'P':
                print("Você perdeu!")
                derrotas += 1
