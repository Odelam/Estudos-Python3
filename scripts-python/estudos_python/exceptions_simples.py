import math

num = int(input("Digite um número inteiro: "))
try:
    print(math.sqrt(num))
except:
    print("Não é um bom valor para raíz quadrada.")
    print("Modificamos o valor para um valor absoluto.")
    print(math.sqrt(abs(num)))

num = int(input("Digite um número inteiro: "))
if num < 0:
    raise RuntimeError ("Você não pode usar um número negativo!")
else:
    print(math.sqrt(num))
