frase = input("Digite algo: ")
primitivo = type(frase)
espaco = frase.isspace()
numero = frase.isnumeric()
alfabetico = frase.isalpha()
alfanumerico = frase.isalnum()
maiusculas = frase.isupper()
minusculas = frase.islower()
capitalizada = frase.istitle()

print(f"O tipo primitivo da variável é: {primitivo}.")
print(f"Só tem espaços? {espaco}.")
print(f"É um número? {numero}.")
print(f"É alfabético? {alfabetico}.")
print(f"É alfanumérico? {alfanumerico}.")
print(f"É maiúscula? {maiusculas}.")
print(f"É minúsculas? {minusculas}.")
print(f"É capitalizada? {capitalizada}.")