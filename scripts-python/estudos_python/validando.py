# while True:
#     nome = str(input("Quém é você? ")).strip().lower().capitalize()
#     if nome != 'Del':
#         continue
#     senha = input(f'Olá, {nome}. Qual é a senha? ')
#     if senha == "peixeespada":
#         break
# print("Acesso liberado!")

nome = ""
while not nome:
    nome = str(input("Digite seu nome: ")).strip().lower().capitalize()
numero_convidados = int(input(f"Olá {nome}. Quantos números de convidados terá? "))

if numero_convidados:
    print("Certifique que terá espaço suficiente para todos os convidados!")
    print(f"Quantidade de convidados: {numero_convidados}.")
    print()
else:
    print(f"Quantidade de convidados: {numero_convidados}.")
    print("Sinto muito.")
    print()
print("Concluído!")