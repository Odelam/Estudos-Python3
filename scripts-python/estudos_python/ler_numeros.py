num = 0
qtd_num = 0
soma = 0
numeros = []

while num != 999:
    num = int(input("Digite um número: [999 - para sair] "))
    if num != 999:
        qtd_num += 1
        soma += num
        numeros.append(num)

print(f"Quantidade de números digitados: {qtd_num}.")
print(f"Soma dos números digitados: {soma}.")
print(f"Os números {numeros}.")

# de uma outra maneira
num1 = cont = 0
soma = 0
num1 = int(input("Digite um número [999 - para sair]: "))
while num1 != 999:
    soma += num1
    cont += 1
    num1 = int(input("Digite um número [999 - para sair]: "))
print(f"Vc digitou {cont} números e a soma entre eles foi {soma}.")
