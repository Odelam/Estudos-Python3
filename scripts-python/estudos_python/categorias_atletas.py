from datetime import date

ano_nasc = int(input("Informe o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
if idade <= 9:
    print("Mirim.")
    print(idade)
elif idade <= 14:
    print("Infantil.")
    print(idade)
elif idade <= 19:
    print("Júnior.")
    print(idade)
elif idade <= 20:
    print("Sênior")
    print(idade)
else:
    print("Master.")
    print(idade)


