continuar = ''
qtd_num = 0
media = 0
numeros = []
num = 0
num_maior = 0
num_menor = 0

while continuar != 'S':
    num = int(input("Digite um número: "))
    qtd_num += 1
    numeros.append(num)
    media = sum(numeros) / len(numeros)
    num_maior = max(numeros)
    num_menor = min(numeros)
    continuar = str(input("Digite [C] para continuar. [S] para sair: ")).strip().upper()

print(f"A média dos números digitados foi: {media}.")
print(f"O maior número digitado foi: {num_maior}.")
print(f"O menor número digitado foi: {num_menor}.")
print(qtd_num)

# de uma outra maneira
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N]: ")).strip()
media = soma / quant
print(f"Vc digitou {quant} de números e a média entre ele foi: {media}.")
print(f"O maior valor foi {maior} e o menor valor foi {menor}.")
