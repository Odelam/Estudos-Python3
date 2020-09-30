import random

alunos = []

while len(alunos) < 4:
    nomes = input("Digite o nome do aluno: ")
    if nomes in alunos:
        print("Nome já digitado!")
        len(alunos) + 1
    else:
        alunos.append(nomes)

escolhido = random.choice(alunos)
print(f"O aluno escolhido foi: {escolhido}.")

