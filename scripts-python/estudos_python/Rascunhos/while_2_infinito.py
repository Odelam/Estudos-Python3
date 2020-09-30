# cont = 1
# while cont <= 10:
#     print(f"{cont} -> ", end='')
#     cont += 1
# print("Fim!")
#
# n = 0
# cont = 0
# soma = 0
# numeros = []
# while cont < 3:
#     n = int(input("Digite um número: "))
#     cont += 1
#     soma += n
#     numeros.append(n)
# print("Soma dos números digitados: ", soma)
# print("Números digitados:", numeros)

n = 0
encerra = ''
numeros = []
while encerra != 'P':
    n = int(input("Digite um número: "))
    numeros.append(n)
    encerra = str(input("Digite [P] para encerrar. Digite [ENTER] para seguir:  ")).strip().upper()
print("Números digitados: ", numeros)

n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print(s)
