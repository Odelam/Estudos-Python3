import random

alunos = []

while len(alunos) < 4:
    nomes = str(input("Digite o nome do aluno: ")).strip().lower().capitalize()
    if nomes in alunos:
        print("Este nome já contém na lista!")
    else:
        alunos.append(nomes)

random.shuffle(alunos)
print(f"Ordem de apresentação: {alunos}.")
