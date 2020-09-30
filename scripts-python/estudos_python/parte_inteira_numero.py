import math

num = float(input("Digite um número: "))

num_int1 = int(num)
num_int2 = math.ceil(num) - 1
num_int3 = math.trunc(num)

print(f"Número: {num}, parte inteira: {num_int1}.")
print(f"Número: {num}, parte inteira: {num_int2}.")
print(f"Usando a função trunc(): {num_int3}.")

