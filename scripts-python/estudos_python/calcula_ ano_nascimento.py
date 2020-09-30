from datetime import date

ano_atual = date.today().year
maior_idade = 0
menor_idade = 0

for c in range(1, 7):
    ano_nasc = int(input(f"Digite o ano em que a {c}ª pessoa nasceu: "))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        maior_idade += 1
    else:
        menor_idade += 1
print()
print(f"Ao todo tivemos {maior_idade} pessoas maiores de idade.")
print(f"Ao todo tivemos {menor_idade} pessoas menores de idade.")
