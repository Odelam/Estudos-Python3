def imprime(lista):
    for i in range(len(lista)):
        print(lista[i])


def recursiva_imprime(lista, i=0):
    if i < len(lista):
        print(lista[i])
        recursiva_imprime(lista, i + 1)


minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Função normal")
imprime(minha_lista)
print()

print("Função recursiva")
recursiva_imprime(minha_lista)
