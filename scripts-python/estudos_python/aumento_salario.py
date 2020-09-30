salario_funcionario = float(input("Digite o salário do funcionário: "))
aumento_tipo_1 = 10
aumento_tipo_2 = 15
salario_key_aumento = 1250

if salario_funcionario <= salario_key_aumento:
    aumento = ((salario_funcionario * aumento_tipo_2) / 100) + salario_funcionario
    print(f"Você recebeu um aumento de {aumento_tipo_2}%.")
    print(f"Salário atual: {aumento:.2f}.")
else:
    aumento = ((salario_funcionario * aumento_tipo_1) / 100) + salario_funcionario
    print(f"Você recebeu um aumento de {aumento_tipo_1}%.")
    print(f"Salário atual: {aumento:.2f}.")
