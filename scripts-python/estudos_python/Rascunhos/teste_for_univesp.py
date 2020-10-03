# lista = ['cachorro', 'gato', 'passarinho', 'coelho']
# for x in lista:
#     print(x)
#
#
# s = "algoritmos"
# for c in s:
#     if c in "aeiou":
#         print(c)
#
#
# for x in range(11): # vai até 10
#     print("Com range", x)
#
# l = ['a', 'b', 'c']
# for i in range(len(l)):
#     print("Imprime até o tamanho da lista", l[i])
#
# for y in range(1, 20, 2):
#     print("Irá imprimir de 1 a 20 pulando de 2 em 2", y)
#
#
# acumulador = 0
# for x in range(1, 101):
#     if x % 2 == 0:
#         acumulador = acumulador + x
#         print(f"Par: {x}.")
# print(f"Total da soma dos números pares: {acumulador:.2f}.")
#
# str_list = ['odelam', 'sá', 'dias']
# for nome in str_list:
#     for letra in nome:
#         if letra in 'aeiouáàâã':
#             print(letra)
#

total = 0
for num in range(101):
    total += num
print(total)
