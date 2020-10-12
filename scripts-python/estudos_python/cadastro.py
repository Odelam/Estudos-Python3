print("*=*" * 20)
print("CADASTRE UMA PESSOA")
print("*=*" * 20)

total_pessoas_maiores = 0
total_homens = 0
mulher_menores_20 = 0

while True:
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo != 'M' and sexo != 'F':
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]

    if idade > 18:
        total_pessoas_maiores += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menores_20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input("Quer continuar? [S/N] ")).upper().strip()[0]

    if resposta == 'N':
        break

print()
print(f"Total de pessoas com mais de 18 anos: {total_pessoas_maiores}.")
print(f"Ao todo temos {total_homens} homem(s) cadastrado no sistema.")
print(f"E temos {mulher_menores_20} mulher(es) menores que 20 anos.")
