encerra = 0

while encerra != 5:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    print('''
    [1] Somar;
    [2] Multiplicar;
    [3] Maior;
    [4] Novos números;
    [5] Sair do programa''')
    escolha = int(input())
    if escolha == 1:
        soma = num1 + num2
        print(f"A soma de {num1} + {num2}: {soma}.")
    elif escolha == 2:
        multi = num1 * num2
        print(f"A multiplicação de {num1} x {num2}: {multi}.")
    elif escolha == 3:
        if num1 > num2:
            print(f"{num1} é maior que {num2}.")
        elif num2 > num1:
            print(f"{num2} é maior que {num1}.")
        else:
            print(f"{num1} e {num2} são iguais!")
    elif escolha == 4:
        numero1 = int(input("digite um novo número: "))
        numero2 = int(input("digite outro número: "))
        print(numero1, numero2)
        print()
    elif escolha == 5:
        print("Fim!")
        break
    else:
        print("Escolha incorreta!")

# de uma outra meneira
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
escolha = 0
while escolha != 5:
    print('''
    [1] - Somar;
    [2] - Multiplicar;
    [3] - Maior;
    [4] - Novos números;
    [5] - Sair do programa.''')
    escolha = int(input(">>>>> Escolha sua opção: "))
    if escolha == 1:
        soma = n1 + n2
        print(f"A soma de {n1} + {n2}: {soma}.")
    elif escolha == 2:
        multi = n1 * n2
        print(f"A multiplicação de {n1} x {n2}: {multi}.")
    elif escolha == 3:
        if n1 > n2:
            maior_numero = n1
            print(f"Entre os números {n1} e {n2} o maior é: {maior_numero}.")
        elif n2 > n1:
            maior_numero = n2
            print(f"Entre os números {n1} e {n2} o maior é: {maior_numero}.")
        else:
            print(f"Os números {n1} e {n2} são iguais.")
    elif escolha == 4:
        print("Informe novos números novamente.")
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
    elif escolha == 5:
        print("Finalizando...")
    else:
        print("Opção inválida! Tente novamente.")
print("Fim.")
