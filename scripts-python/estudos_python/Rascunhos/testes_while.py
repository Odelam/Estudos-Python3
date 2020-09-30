# cont = 0
# while cont < 11:
#     print(cont)
#     cont += 1
# print("Final")
#
# cont = 0
# while cont < 4:
#     num = int(input("Digite um valor: "))
#     cont += 1
#
# n = 1
# while n != 0:
#     n = float(input("Digite um número. Zero cancela a operação."))
# print("fim")
#
# resposta = 'S'
# soma = 0
# while resposta == 'S':
#     num = float(input("Digite um número: "))
#     resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()
#     soma += num
# print(soma)

num = 1
par = impar = 0
numeros_pares = []
numeros_impares = []

while num != 0:
    num = int(input("Digite um número: "))
    if num != 0:
        if num % 2 == 0:
            par += 1
            numeros_pares.append(num)
        else:
            impar += 1
            numeros_impares.append(num)
print(f"{par} foram pares! Números: {numeros_pares}.")
print(f"{impar} foram ímpares! Números: {numeros_impares}.")

