import math

# from math import sqrt, hypot

cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))

hipotenusa1 = math.sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2))
hipotenusa2 = math.hypot(cateto_oposto, cateto_adjacente)
sen = cateto_oposto / hipotenusa1
cos = cateto_adjacente / hipotenusa1
tan = cateto_oposto / cateto_adjacente

print(f"Hipotenusa sem import módulo: {hipotenusa1:.2f}.")
print(f"Hipotenusa com import math: {hipotenusa2}:.2f.")
print()
print(f"Seno: {sen:.2f}.")
print(f"Cosseno: {cos:.2f}.")
print(f"Tangente: {tan:.2f}")
print()

# de uma outra maneira

angulo = float(input("Digite o valor de um ângulo: : "))

sen1 = math.sin(math.radians(angulo))
cos1 = math.cos(math.radians(angulo))
tan1 = math.tan(math.radians(angulo))

print(f"Seno: {sen1:.2f}.")
print(f"Cosseno: {cos1:.2f}.")
print(f"Tangente: {tan1:.2f}.")

