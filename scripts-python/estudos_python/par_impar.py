
cont = 0
while cont < 3:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print(f"O número {numero} é PAR!")
    else:
        print(f"O número {numero} é ÍMPAR!")
    cont += 1
