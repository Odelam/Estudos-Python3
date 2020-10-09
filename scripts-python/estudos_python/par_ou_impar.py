import random

print("=*=" * 20)
print("Vamos jogar par ou ímpar")
print("=*=" * 20)

vitorias_seguidas = 0

while True:
    par_ou_impar = ' '
    while par_ou_impar not in 'PI':
        par_ou_impar = str(input("Par ou Ímpar? [P/I] ")).upper().strip()[0]

    jogada_maquina = random.randint(0, 10)
    jogada_usuario = int(input("Digite um valor: "))
    resultado = jogada_usuario + jogada_maquina
    if par_ou_impar == 'P':
        if resultado % 2 == 0:
            print(f"Você jogou {jogada_usuario} e a máquina {jogada_maquina}.")
            print(f"Total de {resultado} deu PAR.")
            print("Você venceu!")
            vitorias_seguidas += 1

        else:
            print(f"Você jogou {jogada_usuario} e a máquina {jogada_maquina}.")
            print(f"Total de {resultado} deu ÍMPAR.")
            print("Você perdeu!")
            break

    if par_ou_impar == 'I':
        if resultado % 2 == 1:
            print(f"Você jogou {jogada_usuario} e a máquina {jogada_maquina}.")
            print(f"Total de {resultado} deu ÍMPAR.")
            print("Você venceu!")
            vitorias_seguidas += 1

        else:
            print(f"Você jogou {jogada_usuario} e a máquina {jogada_maquina}.")
            print(f"Total de {resultado} deu PAR.")
            print("Você perdeu!")
            break
    print("Vamos jogar novamente...")

print(f"Total de vitórias consecutivas: {vitorias_seguidas}.")
