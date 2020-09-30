nome = str(input("Digite um nome: ")).strip().lower().capitalize()
if nome == 'Odelam':
    print('É um nome bonito e raro.')
elif nome == 'Pedro' or nome == 'Flávia' or nome == 'Jonas':
    print("São nomes bonitos e comuns.")
elif nome in 'Ana Jéssica Eliza':
    print("É um belo nome feminino.")
else:
    print("Seu nome é normal.")
