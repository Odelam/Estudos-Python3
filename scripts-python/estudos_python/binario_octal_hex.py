print('''
[1] - para binário.
[2] - para octal.
[3] - para hexadecimal.
''')
escolha = int(input("Informe sua escolha: "))


def mostra_mgs_escolha():
    if escolha == 1:
        print("Você escolheu Binário.")
    elif escolha == 2:
        print("Você escolheu Octal.")
    elif escolha == 3:
        print("Você escolheu Hexadecimal.")
    else:
        print("Opção inválida.")


mostra_mgs_escolha()

num = int(input("Digite um número: "))

if escolha == 1:
    num_b = bin(num)
    print(f"O número {num} em binário: {num_b[2:]}.")
elif escolha == 2:
    num_o = oct(num)
    print(f"O número {num} em octal é: {num_o[2:]}.")
elif escolha == 3:
    num_hex = hex(num)
    print(f"O número {num} em hexadecimal é: {num_hex[2:]}.")
else:
    print("Opção incorreta!")

# outra maneira de fazer

num1 = int(input("Digite um número inteiro: "))
print('''
[1] - para binário.
[2] - para octal.
[3] - para hexadecimal.''')
opcao = int(input("Digite sua opção: "))
if opcao == 1:
    print("O número {} em Binário é: {}.".format(num1, bin(num1)[2:]))
    print(f"O número {num1} em Binário é: {bin(num1)[2:]}.")
elif opcao == 2:
    print("O número {} em Octal é: {}.".format(num1, oct(num1)[2:]))
elif opcao == 3:
    print("O número {} em Hexadecimal é: {}.".format(num1, hex(num1)[2:]))
else:
    print("Opção inválida!")
