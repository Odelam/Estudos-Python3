# import math
from math import floor, ceil, sqrt
import random
import emoji


num = int(input("Digite um número: "))
raiz = sqrt(num)

print(f"A raiz quadrada de {num} é: {raiz}.")
print(f"Arredondamento pra cima: {ceil(raiz)}.")
print(f"Arredondamento pra baixo: {floor(raiz)}.")

# falando sobre random
num1 = random.randint(1, 10)
print(f"Número gerado de maneira aleatória: {num1}")

# falando sobre biblioteca emoji
print(emoji.emojize("Mostrando emoji :sunglasses:", use_aliases=True))
print(emoji.emojize("Mostrando emoji :alien:", use_aliases=True))
print(emoji.emojize("Mostrando emoji :heart:", use_aliases=True))
print(emoji.emojize("Mostrando emoji :wink:", use_aliases=True))

