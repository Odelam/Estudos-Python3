
preco_produto = float(input("Digite o valor do produto: "))
print('''
[0] - Á vista dinheiro/cheque. 10% de desconto.
[1] - Á vista com cartão. 5% de desconto.
[2] - Em até 2x no cartão.
[3] - 3x ou mais no cartão.''')
escolha = int(input("Informe a forma de pagamento: "))
if escolha == 0:
    preco_desconto = preco_produto - ((preco_produto * 10) / 100)
    print(f"Aplicado 10% de desconto. Preço: R${preco_desconto:.2f}.")
elif escolha == 1:
    preco_desconto = preco_produto - ((preco_produto * 5) / 100)
    print(f"Aplicado 5% de desconto. Preço: R${preco_desconto:.2f}.")
elif escolha == 2:
    parcela = preco_produto / 2
    print(f"Sem descontos! Preço: R${preco_produto:.2f}.")
    print(f" 2 parcelas de R${parcela:.2f}.")
elif escolha == 3:
    preco_produto_juros = ((preco_produto * 20 / 100) + preco_produto)
    parcela = preco_produto_juros / 3
    print(f"3 parcelas de R${parcela:.2f}. Preço: R${preco_produto_juros:.2f}.")
else:
    print(f"Forma de pagamento inválida!")
