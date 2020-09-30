nome = str(input("Digite seu nome completo: ")).strip()

nome_maiuscula = nome.upper()
nome_minuscula = nome.lower()
qtd_letras = len(nome) - nome.count(' ')
primeiro_nome = nome.split()

print(f"Nome em maiúscula: {nome_maiuscula}.")
print(f"Nome em minúsculas: {nome_minuscula}.")
print(f"Quantidade de letras: {qtd_letras}.")
print(primeiro_nome)
print(f"O primeiro nome tem {len(primeiro_nome[0])} letras.")



