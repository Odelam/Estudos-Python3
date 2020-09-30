
cont = 0
while cont < 3:
    velocidade_carro = float(input("Informe a velocidade do veículo: "))
    print()

    limite_velocidade = 80
    multa_por_km = 7

    if velocidade_carro > limite_velocidade:
        valor_multa = (velocidade_carro - limite_velocidade) * multa_por_km
        print(f"Você ultrapassou o limite de velocidade de {limite_velocidade}km/hr.")
        print(f"Foi multado em: {valor_multa:.2f}.")
        print()
    else:
        print(f"Dirija com segurança.")
        print(f"Velocidade registrada: {velocidade_carro}km/hr.")
        print()

    cont += 1
