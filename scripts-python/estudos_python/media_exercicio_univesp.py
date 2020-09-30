print('''Programa simples para calcular média de notas.''')

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))

media = (0.4 * n1) + (0.6 * n2)

if media >= 5.0:
    print(f"Sua média foi: {media:.1f}.")
    print("Aprovado!")
else:
    print(f"Sua média foi: {media:.1f}.")
    print("Reprovado!")

print("Fim da execução.")

