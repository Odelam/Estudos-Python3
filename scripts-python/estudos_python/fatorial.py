from math import factorial
# cont = 1
# fatorial = 1
# num = int(input("Digite um número e descubra seu fatorial: "))
# while cont <= num:
#     fatorial = fatorial * cont
#     cont += 1
#     print(f"O fatorial é {fatorial}.")
#
# # de uma outra maneira
# n = int(input("Digite um número e descubra seu fatorial: "))
# f = factorial(n)
# print(f"O fatorial de {n} é: {f}.")

n = int(input("Digite um número e descubra seu fatorial: "))
c = n
fatorial = 1
print(f"Calculando {n}! = ", end='')
while c > 0:
    print(f"{c}", end='')
    if c > 1:
        print(" x ", end='')
    else:
        print(" = ", end='')
    fatorial *= c
    c -= 1
print(f"{fatorial}.")

n = int(input("Digite um número e descubra seu fatorial: "))
cont = n
for c in range(cont, 0, -1):
    print(f"{c}", end='')
    if c == 1:
        print(" = ", end='')
    elif c > 0:
        print(" x ", end='')
print(factorial(n))
