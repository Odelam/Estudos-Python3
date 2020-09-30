
nota1 = float(input("Informe a nota: "))
nota2 = float(input("Informe outra nota: "))

media = (nota1 + nota2) / 2

if media < 5:
    print(f"{media:.1f}")
    print("REPROVADO!")
elif 5 <= media <= 6.9:
    print(f"{media:.1f}")
    print("RECUPERAÇÃO!")
else:
    print(f"{media:.1f}")
    print("APROVADO!")
