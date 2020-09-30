
nome = input("Qual é seu nome: ")
print("Prazer em te conhecer {:=^20}!".format(nome))
# {:=^20} centraliza e preenche com =.

num = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

soma = num + num2
subtr = num - num2
div_inteira = num // num2
div_float = num / num2
resto_div = num % num2
exponencial = num ** num2
ao_cubo = ((num + num2) ** 1/3)
multiplicacao = num * num2
raiz_quadrada = ((num + num2) ** 1/2)

print(f"A soma de {num} e {num2} é: {soma}.")
print(f"A subtração de {num} e {num2} é: {subtr}.")
print(f"A divisão inteira de {num} e {num2} é: {div_inteira}.")
print(f"A divisão com ponto flutuante de {num} e {num2} é: {div_float:.2f}.")
print(f"O resto da divisão de {num} e {num2} é: {resto_div}.")
print(f"O exponencial de {num} e {num2} é: {exponencial}.")
print(f"O cubo de {num} + {num2} é: {ao_cubo:.2f}.")
print(f"A multiplicação de {num} e {num2} é: {multiplicacao}.")

