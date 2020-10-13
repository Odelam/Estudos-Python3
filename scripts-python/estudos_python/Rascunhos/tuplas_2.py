mamiferos = ('macaco', 'peixe-boi', 'ornitorrinco', 'onça')
print('1')
for animais in range(0, len(mamiferos)):
    print(f"{mamiferos[animais]} é um mamífero.")

print()

print('2')
for animais in mamiferos:
    print(f"{animais} é um mamífero.")

print()

print('3')
for animais in range(0, len(mamiferos)):
    print(f"{mamiferos[animais]} é um mamífero. Posição: {animais}.")

print()

print('4')
for posicao, animais in enumerate(mamiferos):
    print(f"{animais} é um mamífero. Posição: {posicao}.")

print()

print(mamiferos)
print(sorted(mamiferos))
print()

a = (1, 3, 5, 3, 7, 8, 5)
b = (2, 4, 3, 2, 7, 9, 4)
c = a + b
print(c)
print('quantos 3 existe nessa tupla? ', c.count(3))
print('Qual é a posição do número 5? ', c.index(5))
print('A tupla é imutável mas podemos apagar ela por inteiro. Lembrando que não é possível apagar apenas 1 elemento dela.')