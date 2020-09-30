pesos = []
for c in range(1, 6):
    peso = float(input(f"Informe o peso da {c}ª pessoa: "))
    pesos.append(peso)

peso_maximo = max(pesos)
peso_minimo = min(pesos)
print()
print(f"O menor peso encontrado foi: {peso_minimo:.2f}Kg.")
print(f"O maior peso encontrado foi: {peso_maximo:.2f}Kg.")

# outra maneira de fazer
maior = 0
menor = 0
for p in range(1, 7):
    peso = float(input(f"Informe o peso da {p}ª pessoa: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print()
print(f"O maior peso lido foi de {maior}Kg.")
print(f"O menor peso lido foi de {menor}.Kg")
