from datetime import date

ano = int(input("Digite um ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é Bissexto!")
else:
    print(f"O ano {ano} não é Bissexto!")


# outra maneira de se fazer
ano1 = int(input("Qual ano deseja analisar? Digite 0 para analisar o ano atual."))

if ano1 == 0:
    ano1 = date.today().year
if ano1 % 4 == 0 and ano1 % 100 != 0 or ano1 % 400 == 0:
    print(f"O ano {ano1} é Bissexto!")
else:
    print(f"O ano {ano1} não é Bissexto!")
