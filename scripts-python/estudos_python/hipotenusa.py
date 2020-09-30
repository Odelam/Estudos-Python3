from math import sqrt, hypot

cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))

hipotenusa1 = sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2))
hipotenusa2 = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
hipotenusa3 = hypot(cateto_oposto, cateto_adjacente)

print(f"Hipotenusa sem import módulo: {hipotenusa1:.2f}.")
print(f"Hipotenusa com import math: {hipotenusa3}:.2f")
print(f"Hipotenusa na fórmula: {hipotenusa2}:.2f.")
