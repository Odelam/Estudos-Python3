
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"{imc:.2f}.")
    print("Peso abaixo do normal. Neste caso, é necessária a busca por um especialista, para verificar a existência "
          "de algum problema de saúde causador do índice abaixo do normal, "
          " ou analisar se sua saúde não está sendo afetada.")
elif 18.5 <= imc <= 24.9:
    print(f"{imc:.2f}.")
    print("São pesos considerados normais pela OMS. No entanto, mesmo nesta faixa de peso,"
          " deve-se ter atenção e cuidado com possíveis problemas metabólicos, principalmente se houver acúmulo"
          " de gordura na região interna do abdômen")
elif 25 <= imc <= 29.9:
    print(f"{imc:.2f}.")
    print("Peso em pré-obesidade ou acima do peso, representando um risco maior para a saúde. "
          "Nesta causa, é imprescindível uma consulta com um especialista, pois pode estar relacionado à pressão alta,"
          " colesterol alto ou diabetes, podendo apontar até para o hipotireoidismo. Este é o seu índice? Se sim, "
          "é tempo de consultar um profissional, realizar exames e pensar em uma reeducação alimentar e exercícios "
          "físicos.")
elif 30 <= imc <= 39.9:
    print(f"{imc:.2f}.")
    print("Indica obesidade grau dois. Este peso já representa risco elevado para as doenças supracitadas. Como em "
          "todos os casos, mas neste impreterivelmente, deve-se buscar um profissional especializado e receber as "
          "orientações e medidas adequadas para obter uma saúde equilibrada.")
else:
    print(f"{imc:.2f}.")
    print("Indica obesidade grau três ou mórbida. O peso neste grau apresenta problemas extremamente graves e "
          "necessita de tratamento profissional com o máximo de recursos disponíveis, incluindo até cirurgia.")
