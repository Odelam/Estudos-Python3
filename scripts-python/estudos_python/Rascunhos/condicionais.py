print(f"Alguns exemplos de condicionais.")
nome = str(input("Digite seu nome: ")).strip().lower().capitalize()

if nome == "Odelam":
    print(f"Bem vindo, {nome}.")
else:
    print(f"Usuário não encontrado!")
print("Fim")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media >= 6.9:
    print(f"A média da nota foi: {media:.2f}.")
    print("APROVADO!")
else:
    print(f"A média da nota foi: {media:.2f}.")
    print("REPROVADO!")

