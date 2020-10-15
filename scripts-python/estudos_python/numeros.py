import random

num1 = (random.randint(0, 10))
num2 = (random.randint(0, 20))
num3 = (random.randint(0, 30))
num4 = (random.randint(0, 5))
num5 = (random.randint(0, 7))

lista_aleatory = (num1, num2, num3, num4)
minimo = min(lista_aleatory)
maximo = max(lista_aleatory)

print("Os números sorteados foram:", end=' ')
for n in lista_aleatory:
    print(n, sep=',', end=' ')

print()
print(f"O menor número é: {minimo}.")
print(f"O maior número é: {maximo}.")
