import random

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''
[0] - para Pedra.
[1] - para Papel.
[2] - para Tesoura.''')
jogador = int(input("Qual é a sua jogada: "))
if jogador > 2:
    print("Escolha inválida!")
else:
    print()

    print("Computador escolheu:", itens[computador])
    print("usuário escolheu:", itens[jogador])
    print()

    if computador == 0: # computador jogou pedra
        if jogador == 0:
            print("Empate!")
        elif jogador == 1:
            print("Você Venceu!")
        elif jogador == 2:
            print("Computador Venceu!")
        else:
            print("Jogada inválida!.")
    elif computador == 1: # computador jogou papel
        if jogador == 0:
            print("Computador Venceu!")
        elif jogador == 1:
            print("Empate!")
        elif jogador == 2:
            print("Você Venceu!")
        else:
            print("Jogada inválida!")
    elif computador == 2: # computador jogou tesoura
        if jogador == 0:
            print("Você Venceu!")
        elif jogador == 1:
            print("Computador Venceu!")
        elif jogador == 2:
            print("Empate!")
        else:
            print("Jogada inválida!")
