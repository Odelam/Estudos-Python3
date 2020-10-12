

print("*" * 20)
print("O Lojinha")
print("*" * 20)

total_compra = 0
mais_de_mil = 0
menor = cont = 0
base_preco_alto = 1000
barato = ''

while True:
    nome_produto = str(input("Nome do produto: ")).strip().title()
    preco = float(input("Preço: R$"))
    cont += 1
    total_compra += 1
    if preco > 1000:
        mais_de_mil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = nome_produto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if resposta == 'N':
        break

print()
print(f"O total da compra foi R$:{total_compra:.2f}.")
print(f"Temos {mais_de_mil:.2f} custando mais de R${base_preco_alto:.2f}.")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}.")
print('-' * 10,'Fim do programa',10 * '-')