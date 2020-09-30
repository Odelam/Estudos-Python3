import random

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''
[0] - para Pedra.
[1] - para Papel.
[2] - para Tesoura.''')
jogador = int(input("Qual é a sua jogada: "))
print()
if jogador > 2:
    print("Jogada inválida!")
else:

    print("Computador escolheu:", itens[computador])
    print("usuário escolheu:", itens[jogador])
    print()

    if computador == 0 and jogador == 0:
        print("Empate!")
    elif computador == 0 and jogador == 1:
        print("Você Venceu!")
    elif computador == 0 and jogador == 2:
        print("Computador Venceu!")

    elif computador == 1 and jogador == 0:
        print("Computador Venceu!")
    elif computador == 1 and jogador == 1:
        print("Empate!")
    elif computador == 1 and jogador == 2:
        print("Você Venceu!")

    elif computador == 2 and jogador == 0:
        print("Você Venceu!")
    elif computador == 2 and jogador == 1:
        print("Computador Venceu!")
    elif computador == 2 and jogador == 2:
        print("Empate!")
    else:
        print("Jogada Inválida!")

