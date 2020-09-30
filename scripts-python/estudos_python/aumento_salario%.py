
salario = float(input("Digite o salário: "))
aumento_percent = 15

salario_ajuste = (salario * aumento_percent / 100) + salario

print(f"O salario de {salario:.2f} com 15% de aumento: {salario_ajuste:.2f}.")
