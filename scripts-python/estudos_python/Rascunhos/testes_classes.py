import random

# class Minha_Lista:
#     def __init(self, inicial=()):
#         self.lista = inicial
#
#     def __len__(self):
#         return len(self.lista)
#
#     def adiciona(self, item):
#         self.lista.append(item)
#
#
# lista_1 = Minha_Lista()
# lista_1.adiciona(1)
# lista_1.adiciona("dois")
# lista_1.adiciona(3)
# tamanho_lista = lista_1.__len__()
#
# print(lista_1)
# print(tamanho_lista)

import random


class MinhaLista(list):
    def escolha(self):
        return random.choice(self)


lista1 = MinhaLista()
lista1.append(2)
lista1.append("três")
lista1.append(4)
print(lista1.escolha())