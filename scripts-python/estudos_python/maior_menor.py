import math

numeros = []

while len(numeros) < 3:
    numero_usuario = int(input("Digite um número: "))
    if numero_usuario in numeros:
        print("Número já selecionado!")
    else:
        numeros.append(numero_usuario)

print(f"O número maior é: {max(numeros)}.")
print(f"O número menor é: {min(numeros)}")
print(f"Números: {numeros}.")

# outra maneira de fazer

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

# verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c

print(f"O menor valor digitado foi: {menor}.")
print(f"O maior valor digitado foi: {maior}.")
