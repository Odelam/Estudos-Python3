print("Cores no texto:")
print(f"\033[30m Olá Mundo!\033[m.")
print(f"\033[31m Olá Mundo!\033[m.")
print(f"\033[32m Olá Mundo!\033[m.")
print(f"\033[33m Olá Mundo!\033[m.")
print(f"\033[34m Olá Mundo!\033[m.")
print(f"\033[35m Olá Mundo!\033[m.")
print(f"\033[36m Olá Mundo!\033[m.")
print(f"\033[37m Olá Mundo!\033[m.")
print()
print("Cores no background:")
print("Adicionei cores em alguns textos para ficar mais legível.")
print(f"\033[31;40m Olá Mundo!\033[m.")
print(f"\033[30;41m Olá Mundo!\033[m.")
print(f"\033[34;42m Olá Mundo!\033[m.")
print(f"\033[34;43m Olá Mundo!\033[m.")
print(f"\033[30;44m Olá Mundo!\033[m.")
print(f"\033[30;45m Olá Mundo!\033[m.")
print(f"\033[31;46m Olá Mundo!\033[m.")
print(f"\033[30;47m Olá Mundo!\033[m.")
print()
print("Aplicado o style sem background:")
print(f"\033[0m Olá Mundo!\033[m.")
print(f"\033[1m Olá Mundo!\033[m.")
print(f"\033[4m Olá Mundo!\033[m.")
print(f"\033[7m Olá Mundo!\033[m.")
print(f"\033[0m Olá Mundo!\033[m.")
print(f"\033[1m Olá Mundo!\033[m. Bold")
print(f"\033[4m Olá Mundo!\033[m. Sublinhado")
print(f"\033[7m Olá Mundo!\033[m. Fundo branco")
print()
print("Aplicando todos os estilos:")
print(f"\033[0;30;44m Deixando estilo como 0 e a cor do texto como branco e o background de azul.\033[m")
print()

print("Definir variáveis para as cores.")
cores = {'limpa': '\033[m',
         'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'azul-claro': '\033[36m',
         'cinza': '\033[37',
         'back_branco': '\033[30m',
         'back_vermelho': '\033[31m',
         'back_verde': '\033[32m',
         'back_amarelo': '\033[33m',
         'back_azul': '\033[34m',
         'back_roxo': '\033[35m',
         'back_azul-claro': '\033[36m',
         'back_cinza': '\033[37'}

nome = "Odelam"
print(f"Olá {cores['azul']}{nome}{cores['limpa']}! Bem vindo!")
