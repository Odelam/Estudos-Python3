nome = str(input("Digite seu nome completo: ")).strip().lower().capitalize()
print(nome)
sobrenome = "silva"

if sobrenome in nome:
    print(f"Seu nome contém o sobrenome '{sobrenome}'.")
else:
    print(f"Seu nome não contém o sobrenome '{sobrenome}'.")
