# for c in range(1, 11):
#     print(c)
# print("Ordem crescente.")
# print()
#
# for c in range(11, 0, -1):
#     print(c)
# print("Ordem decrescente")
# print()
#
# for c in range(1, 11, 2):
#     print(c)
# print("Pulando de 2 em 2")
#
# i = int(input("Início: "))
# f = int(input("Fim: "))
# p = int(input("Passo: "))
# for c in range(i, f + 1, p):
#     print(c)
# print("Fim.")
#
# soma = 0
# for c in range(1, 4):
#     num = int(input("Digite um número: "))
#     soma = soma + num
# print(soma)

lista_palavras = ["gato", "cachorro", "papagaio"]
lista_letra = []
letras_repetidas = []
for palavra in lista_palavras:
    for letra in palavra:
        if letra not in lista_letra:
            lista_letra.append(letra)
        else:
            letras_repetidas.append(letra)
print("Letras que aparecem apenas uma vez: ", lista_letra)
print("Letras que aparecem mais de uma vez: ", letras_repetidas)
print(lista_palavras)