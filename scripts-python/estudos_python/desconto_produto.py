
preco = float(input("Informe o preço do produto: "))

taxa_desconto = 5
preco_desconto = preco - (preco * taxa_desconto / 100)

print(f"O produto custava R${preco:.2f}, na promoção com {taxa_desconto}% vai custar R${preco_desconto:.2f}.")
