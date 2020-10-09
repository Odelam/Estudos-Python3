
while True:
    multiplica = int(input("Quer ver a tabuada de qual valor? "))
    if multiplica < 0:
        print("Tem certeza que deseja sair?")
        resposta = str(input("[S/N]: ")).upper().strip()
        if resposta == 'S':
            print("Programa encerrado.")
            break
        else:
            multiplica = int(input("Quer ver a tabuada de qual valor? "))
    for numero in range(0, 11):
        print(f"{multiplica} x {numero} = {numero * multiplica}.")
    print()