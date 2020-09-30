
soma = 0
contador = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c
        contador = contador + 1

print(f"A soma de todos os {contador} valores ímpares divisível por 3, é: {soma}.")
