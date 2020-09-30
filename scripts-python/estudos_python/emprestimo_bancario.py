import time

valor_casa = float(input("Digite o valor da casa R$: "))
salario_comprador = float(input("Digite o salario do comprador R$: "))
anos_pagamento = int(input("Digite em quantos anos de financiamento: "))
print()

meses = anos_pagamento * 12
prestacao = valor_casa / meses
percent_salario = (salario_comprador * 30) / 100

print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos_pagamento} anos.")
print("Processando...")
time.sleep(2)
print()

if prestacao <= percent_salario:
    print(f"Empréstimo concedido!")
    print(f"Financiamento de {anos_pagamento} anos. Valor da parcela: R${prestacao:.2f}.")
else:
    print("Empréstimo negado!")
