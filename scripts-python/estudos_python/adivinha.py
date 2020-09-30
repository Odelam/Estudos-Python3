import random
from time import sleep

numero_secreto = random.randint(0, 5)
print("Número secreto:", numero_secreto)

numero_usuario = int(input("Digite um número de 0 a 5 e tente adivinhar o número da máquina: "))
print("Processando...")
sleep(2)

if numero_usuario == numero_secreto:
    print(f"Parabéns! Você acertou!")
    print(f"Seu número: {numero_usuario}.")
    print(f"Número do computador: {numero_secreto}.")
else:
    print("Você perdeu!")

