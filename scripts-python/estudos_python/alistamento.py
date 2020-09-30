from datetime import date

ano_nascimento = int(input("Digite o ano em que nasceu: "))
print()

ano_atual = date.today().year
idade = ano_atual - ano_nascimento
idade_de_alistamento = 18

if idade < idade_de_alistamento:
    tempo_para_alistamento = idade_de_alistamento - idade
    ano_alistamento = ano_atual + tempo_para_alistamento

    print(f"Você ainda vai se alistar")
    print(f"Ainda falta {tempo_para_alistamento} anos.")
    print(f"Irá se alistar no ano de {ano_alistamento}.")
elif idade > idade_de_alistamento:
    tempo_atrasado = idade - idade_de_alistamento
    ano_alistamento = ano_atual - tempo_atrasado

    print(f"Você passou do tempo de se alistar!")
    print(f"Está a {tempo_atrasado} anos atrasado.")
    print(f"Deveria ter se alistado no ano de {ano_alistamento}.")
elif idade == idade_de_alistamento:
    print(f"Você tem {idade} e está na hora de se alistar.")
    print(f"Deve se alistar neste ano de {ano_atual}.")
else:
    print("Ano inválido!")
