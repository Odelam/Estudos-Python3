# lista = [1024, 3, True, 6.5]
#
# lista.append(False)
# lista.insert(2, 4.5)
# print(lista)
# print(lista.pop())
# print(lista)
# print(lista.pop(1))
# print(lista)
# lista.sort()
# print(lista)
# lista.reverse()
# print(lista)

print(range(10))
print(list(range(10)))
print(range(10))
print(list(range(5, 10)))
print(list(range(0, 10, 2)))
print(list(range(10, -1, -1)))

minha_lista = {3, 6, 2, "gato", 4.5, False}
minha_lista_2 = {4, 7, 2, "cão", 5.5, True}
print(minha_lista)
print(minha_lista_2)
print('gato' in minha_lista)
print("Retorna um novo conjunto com todos os elementos de ambos os conjuntos", minha_lista | minha_lista_2)
print("Retorna um novo conjunto com apenas os elementos comuns a ambos", minha_lista & minha_lista_2)
print("Retorna um novo conjunto com todos os itens do primeiro conjunto, não do segundo", minha_lista - minha_lista_2)
print("Retorna um novo conjunto com todos os itens do primeiro conjunto, não do segundo", minha_lista_2 - minha_lista)
print("Pergunta se todos os elementos do primeiro conjunto estão no segundo", minha_lista <= minha_lista_2)
print("Retorna um novo conjunto com todos os elementos de ambos os conjuntos", minha_lista.union(minha_lista_2))
print("Retorna um novo conjunto com apenas os elementos comuns a ambos os conjuntos", minha_lista.intersection(minha_lista_2))
print("Retorna um novo conjunto com todos os itens do primeiro conjunto, não no segundo", minha_lista.difference(minha_lista_2))
print("Pergunta se todos os elementos de um conjunto estão no outro", minha_lista.issubset(minha_lista_2))
minha_lista.add("trovão")
print("Adiciona um item ao conjunto", minha_lista)
minha_lista.remove("gato")
print("Remove item do conjunto", minha_lista)
print("Remove e retorna pra gente o último item do conjunto", minha_lista.pop())
print(minha_lista)
minha_lista.clear()
print("Remove todos os itens do conjunto", minha_lista)





