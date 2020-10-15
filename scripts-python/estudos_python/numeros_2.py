lista_numeros = []
numero = ''

for n in range(0, 4):
    numero = int(input("Digite um número: "))
    lista_numeros.append(numero)

lista_numeros = tuple(lista_numeros)
print()

if 9 in lista_numeros:
    print(f"O numero 9 apareceu {lista_numeros.count(9)} vezes.")
else:
    print("Essa lista não possui o número 9.")

if 3 in lista_numeros:
    print(f'O número 3 apareceu na {lista_numeros.index(3)}ª posição.')
else:
    print('Essa lista não possui o número 3.')

print('Os valores pares digitados foram: ', end='')
for p in lista_numeros:
    if p % 2 == 0:
        print(p, sep=',', end=' ')
print()
