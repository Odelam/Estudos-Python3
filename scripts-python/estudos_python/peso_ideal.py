
print('''Descubra seu peso ideal:
[1] - Para homem;
[2] - Para mulher;''')
sexo = int(input("Informe seu sexo: "))
altura = float(input("Informe sua altura: "))

if sexo == 1:
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é: {peso_ideal:.2f}.")
elif sexo == 2:
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {peso_ideal:.2f}.")
else:
    print("Sexo não encontrado!")

print("Fim da execução")