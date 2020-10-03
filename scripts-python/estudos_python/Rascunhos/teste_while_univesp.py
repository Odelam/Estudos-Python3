# def nfat(L):
#     n = 0
#     fat = 1
#     while fat <= L:
#         n += 1
#         fat *= n
#     return n - 1
#
#
# print(f"O fatorial é: {nfat(20)}")
#
# num = int(input("Digite um número positivo: "))
# while num < 0:
#     print("Número incorreto!")
#     num = int(input("Digite um número positivo: "))
#
# lista = []
# nome = str(input("Digite um nome: ")).strip().lower().capitalize()
# print("Ou aperte enter para sair.")
# print()
#
# while nome != '':
#     lista.append(nome)
#     nome = str(input("Digite um nome: ")).strip().lower().capitalize()
#     print("Ou aperte enter para sair.")
#
# for nomes in lista:
#     print(f"Pessoas da lista: {nomes}.")
#
#
# def primo(num):
#     i = 2
#     while i < num:
#         if num % i == 0:
#             print(num)
#             break
#         i += 1
#     return i == num
#
#
# num = int(input("Digite um número e descubra se ele é primo: "))
# print(primo(num))
#
#
# print("Imprimir números primos do 2 ao 100")
# for n in range(2, 15):
#     if not primo(n):
#         continue
#     print(n)

print("Meu nome é: ")
cont = 0
while cont < 5:
    print(f"Del 5 vezes {cont}")
    cont += 1
