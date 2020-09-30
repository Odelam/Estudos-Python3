
num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))

if num1 > num2:
    print(f"O primeiro número '{num1}' é maior.")
elif num2 > num1:
    print(f"O segundo número '{num2}' é maior.")
else:
    print(f"Não existe número maior. Os dois valores são iguais.")
    print(f"Primeiro valor: '{num1}'.")
    print(f"Segundo valor: '{num2}'.")

