import random

print("=*=" * 20)
print("Vamos jogar par ou ímpar")
print("=*=" * 20)

vitorias_seguidas = 0
empates = 0

while True:
    jogada_maquina = random.randint(0, 11)
    par_ou_impar = str(input("Par ou Ímpar? [P/I] ")).upper().strip()
    jogada_usuario = int(input("Digite um valor: "))
    if par_ou_impar == 'P':
        resultado = jogada_usuario + jogada_maquina
        if resultado % 2 == 0:
            print(f"Você jogou {jogada_usuario} e a máquina {jogada_maquina}.")
            print(f"Total de {resultado} deu PAR.")
            print("Você venceu!")
            vitorias_seguidas += 1

        elif resultado % 2 == 0 and jogada_maquina % 2 == 0 and jogada_usuario % 2 == 0:
            print("Empate!")
            empates += 1

        else:
            print(f"Você jogou {jogada_usuario} e a máquina {jogada_maquina}.")
            print(f"Total de {resultado} deu ÍMPAR.")
            print("Você perdeu!")
            break

    if par_ou_impar == 'I':
        resultado = jogada_usuario + jogada_maquina
        if resultado % 2 == 1:
            print(f"Você jogou {jogada_usuario} e a máquina {jogada_maquina}.")
            print(f"Total de {resultado} deu ÍMPAR.")
            print("Você venceu!")
            vitorias_seguidas += 1

        elif resultado % 2 == 1 and jogada_maquina % 2 == 1 and jogada_usuario % 2 == 1:
            print("Empate!")
            empates += 1

        else:
            print(f"Você jogou {jogada_usuario} e a máquina {jogada_maquina}.")
            print(f"Total de {resultado} deu PAR.")
            print("Você perdeu!")
            break
print(f"Total de vitórias consecutivas: {vitorias_seguidas}.")
print(f"Total de empates: {empates}.")