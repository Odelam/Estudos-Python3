sexo = str(input("Digite seu sexo [F/M]: ")).strip().upper()[0]
while sexo != 'F' and sexo != 'M':
    print("Sexo incorreto!")
    sexo = str(input("Digite seu sexo: [F/M] ")).strip().upper()[0]
print("Seu sexo é:", sexo)

# de uma outra maneira
sexo = str(input("informe seu sexo [M/F] :")).strip()[0]
while sexo not in 'MmFf':
    print("Escolha incorreta!")
    sexo = str(input("informe seu sexo [M/F]:")).strip()[0]
print(f"Sexo {sexo} registrado com sucesso!")


