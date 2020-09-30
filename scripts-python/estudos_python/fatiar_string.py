frase = str(input("Digite uma frase: ")).strip().lower()

qtd_letra = frase.count('a')
primeira_posicao = frase.find('a') + 1
ultima_posicao = frase.rfind('a') + 1

print(frase)
print("Quantas vezes aparece a letra 'a': ", qtd_letra)
print(f"A primeira letra 'a' apareceu na posição: {primeira_posicao}.")
print(f"A última letra 'a' apareceu na posição: {ultima_posicao}.")
print('''Para ṕegar a última letra 'a' que aparece na frase nós utilizamos a função rfind()
que nos permite contar os índices da direita para a esquerda.''')