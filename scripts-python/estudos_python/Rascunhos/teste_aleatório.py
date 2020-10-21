import statistics


#
# def func(x, y):
#     x, y = y, x
#
#
# x = 2
# y = 3
# func(x, y)
#
# print(x, y)
#
#
# def media_harmonica():
#     nt1 = float(input("Digite a primeira nota: "))
#     nt2 = float(input("Digite a segunda nota: "))
#     nt3 = float(input("Digite a terceira nota: "))
#
#     media_harmonica = 3 / ((1 / nt1) + (1 / nt2) + (1 / nt3))
#     if media_harmonica >= 5:
#         print(f"Parabéns! Você passou! Nota:{media_harmonica:.1f}.")
#     else:
#         print(f"Você reprovou! Nota:{media_harmonica:.1f}")
#
#
# media_harmonica()
#

# lista = ['cão', 'gato', 'peixe']
# lista_letra = []
# for palavra in lista:
#     for letra in palavra:
#         if letra not in lista_letra:
#             lista_letra.append(letra)
# print(lista_letra)

# def imprime_vogal(palavra_escolhida):
#     lista_letra = []
#     for palavra in palavra_escolhida:
#         for letra in palavra:
#             if letra in 'aeiou':
#                 lista_letra.append(letra)
#     print(lista_letra)
#
#
# imprime_vogal("macaco")

# def mutabilidade(lista):
#     lista[0] = 5
#     return lista
#
#
# minha_lista = [3, 6, 9, 12]
# print(mutabilidade(minha_lista))
# print(minha_lista)

# def mutabilidade(x):
#     x = 5
#     return x
#
# a = 3
# print(mutabilidade(a))
# print(a)
#
time = ['a', 'b', 'c', 'd', 'e']
time.reverse()
print(time)
