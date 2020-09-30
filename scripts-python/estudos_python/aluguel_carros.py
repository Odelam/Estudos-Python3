
km_percorrido = float(input("Informe a quantidade de km percorrido: "))
qtd_dia_alugado = int(input("Informe a quantidade de dias que ficou com o carro: "))

diaria_carro = 60
preco_km_rodado = 0.15

km_a_pagar = km_percorrido * preco_km_rodado
preco_total_diaria = qtd_dia_alugado * diaria_carro
total_aluguel = km_a_pagar + preco_total_diaria

print(f"preço da quilometragem: {km_a_pagar:.2f}.")
print(f"preço das diárias: {preco_total_diaria:.2f}.")
print(f"Total do custo do aluguel: R${total_aluguel:.2f}.")
