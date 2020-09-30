
frase = str(input("Digite uma frase e descubra se ela é um palíndromo: ")).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("Palíndromo")
    print(frase, inverso)
else:
    print("Não é um Palíndromo")

# de uma outra maneira
frase = str(input("Digite uma frase e descubra se ela é um palíndromo: ")).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f"O inverso de {junto}, é: {inverso}.")
if inverso == junto:
    print("Palíndromo")
else:
    print("Não é um Palíndromo")
