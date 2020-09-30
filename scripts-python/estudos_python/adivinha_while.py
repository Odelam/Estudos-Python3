import random
from time import sleep

numero_secreto = random.randint(0, 10)
print("Número secreto:", numero_secreto)
tentativas = 0
numero_usuario = -1

while numero_secreto != numero_usuario:
    numero_usuario = int(input("Digite um número de 0 a 10 e tente adivinhar o número da máquina: "))
    print("Processando...")
    sleep(2)
    tentativas += 1
    print()
    if numero_usuario == numero_secreto:
        print(f"Parabéns! Você acertou!")
        print(f"Seu número: {numero_usuario}.")
        print(f"Número do computador: {numero_secreto}.")
        print(f"Precisou de {tentativas} tentativas para acertar.")
    else:
        print("Você perdeu!")

# de uma outra maneira
computador = random.randint(0, 10)
print("O computador acabou de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual é?")
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input("Qual é seu palpite: "))
    tentativas += 1
    print()
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("O número é maior. Tente outra vez!")
        elif jogador > computador:
            print("O número é menor. Tente outra vez!")

print(f"Você precisou de {tentativas} para acertar!")
print(f"O número do computador foi: {computador}.")