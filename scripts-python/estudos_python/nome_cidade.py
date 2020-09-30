nome_cidade = str(input("Digite o nome da cidade: ")).strip().lower().split()
print(nome_cidade)

if nome_cidade[0] in "santo":
    print(f"A cidade começa com a palavra 'Santo'.")
else:
    print("Sua cidade não começa com 'Santo'.")
