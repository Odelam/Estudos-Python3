
quantidade_numero = 0
soma = 0

while True:
    numero = int(input("Informe números inteiros (999 para sair): "))
    if numero != 999:
        soma += numero
        quantidade_numero += 1
    else:
        print("Tem certeza que deseja sair? [S/N]")
        resposta = str(input()).upper().strip()
        if resposta == 'S':
            break
        else:
            numero = int(input("Informe números inteiros: "))
            soma = soma + numero
            quantidade_numero += 1

print(f"A soma dos números: {soma}.")
print(f"Quantidade de números digitados: {quantidade_numero}.")

# outra maneira de se fazer

soma = contador = 0
while True:
    num = int(input("Digite um valor (999 para sair): "))
    if num == 999:
        break
    contador += 1
    soma += num

print(f"A soma dos números foi: {soma}. E a quantidade de números digitados: {contador}.")