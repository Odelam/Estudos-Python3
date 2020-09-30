sqlista = []
for n in range(1, 11):
    sqlista.append(n * n)
print(sqlista)

print("Usando compreensão de lista:")
sqlista = [c * c for c in range(1, 11)]
print(sqlista)

print("Mais um exemplo de compreensão de lista:")
sqlista = [n * n for n in range(1, 11) if n % 2 != 0]
print(sqlista)

lista = ['cão', 'gato', 'peixe']
lista_letra = []
for palavra in lista:
    for letra in palavra:
        if letra not in lista_letra:
            lista_letra.append(letra)
print(lista_letra)

