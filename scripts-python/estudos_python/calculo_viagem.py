import datetime

km_viagem = float(input("Digite a distância da viagem: "))
limite_km_01 = 200
preco_por_km_01 = 0.50
preco_por_km_02 = 0.45

if km_viagem <= limite_km_01:
    preco_passagem = km_viagem * preco_por_km_01
    print(f"Valor da passagem: {preco_passagem:.2f}.")
    print("tipo 1")
    print()
else:
    preco_passagem = km_viagem * preco_por_km_02
    print(f"Valor da passagem: {preco_passagem:.2f}.")
    print()

print("Bom dia!")
print("Dia", datetime.datetime.now())
