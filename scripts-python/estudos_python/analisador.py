soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_domaisvelho = ''
mulheres_menores = 0

for c in range(1, 5):
    print(f"-----{c}ª Pessoa -----")
    nome = str(input("Nome: ")).strip().capitalize()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    soma_idade += idade

    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_domaisvelho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_domaisvelho = nome
    if idade < 20 and sexo in 'Ff':
        mulheres_menores += 1

media_idade = soma_idade / 4
print()
print(f"A média de idade do grupo é {media_idade:.0f} anos.")
print(f"O homem mais velho tem {maior_idade_homem} anos e seu nome é {nome_domaisvelho}")
print(f"Temos {mulheres_menores} menores que 20 anos no grupo.")
