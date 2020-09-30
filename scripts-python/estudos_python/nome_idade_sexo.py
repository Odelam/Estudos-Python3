nome = []
idade = []
sexo = []
media = 0
for c in range(1, 3):
    nome.append(str(input("Digite seu nome: ")).strip().lower())
    idade.append(int(input("Digite sua idade: ")))
    sexo.append(str(input("Informe seu sexo. [M] - para masculino, [F] - para feminino.")).strip().upper())

for c in range(len(idade)):
    media = idade[c] + len(idade) - 1 / len(idade) - 1

print(media)


