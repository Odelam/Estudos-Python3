frase_0 = "Curso em vídeo em python"
print(f"Existem {frase_0.upper().count('O')} letras 'o' dentro da frase: '{frase_0}'.")
print()

frase_1 = "Ciência de Dados com Python"
print(f"A frase: '{frase_1}' tem {len(frase_1)} caracteres.")
print()

frase_2 = "     Programando em python     "
print(f"Frase: '{frase_2}'.")
print(f"Sem strip(): {len(frase_2)}")
print(f"Com strip(): {len(frase_2.strip())}")
print(f"A função strip() remove espaços em brancos antes e depois da frase: '{frase_2}'.")
print(f"Deixando a frase assim: {frase_2.strip()}")
print()

frase_3 = "Python é uma linguagem muito legal!"
print(f"Frase: '{frase_3}'")
print(f"Utilizando o replace(): {frase_3.replace('Python', 'C++')}")
print(f"Trocamos o 'Python' por 'C++' utilizando o replace().")
print()
print(f"strings em python são imutáveis, mas conseguimos manipulá-las com algumas funções.")
frase_4 = "Frase original"
frase_4_modificada = frase_4.replace("original", "modificada")
print(f"{frase_4_modificada}. Frase modificada por replace e guardada em uma variável.")
print()
print('''Para saber se uma string está dentro de uma variável podemos fazer isso com a função in. Veja:''')
frase_5 = "Podemos fazer muitas coisas com Python."
print(f"Frase: '{frase_5}'.")
print("A palavra 'Python' está dentro dessa frase?", 'Python' in frase_5)
print(f"Frase: '{frase_5}'.")
print("A palavra 'C++' está dentro dessa frase?", 'C++' in frase_5)
print()
print('''Para encontrar a posição em que uma palavra se encontra podemos utilizar a função find()''')
frase_5 = "Podemos fazer sites, jogos, Apps e trabalhar com Big Data com python!"
print(f"Dê uma olhada na frase: '{frase_5}'")
print(f"Vamos ver em qual posição a palavra 'Big' se encontra.")
print(f"A palavra 'Big' se contra na posição: {frase_5.find('Big')}.")
print(frase_5[49:53])
print()
print('''Utilizando o split(). Ele transforma a nossa frase em uma espécie de lista.''')
frase_6 = "Usando python na mineração de dados.".split()
frase_6_original = "Usando python na mineração de dados."
print(f"Veja uma frase com split():")
print(frase_6)
print(f"Frase original: {frase_6_original}.")
print()
print('''Depois que uma frase está com split() podemos acessar cada frase com índices.''')
print(frase_6)
print(f"posição 0: {frase_6[0]}")
print(f"posição 1: {frase_6[1]}")
print(f"posição 2: {frase_6[2]}")
print(f"posição 3: {frase_6[3]}")
print(f"posição 4: {frase_6[4]}")
print(f"posição 5: {frase_6[5]}")
print('''Podemos acessar as letras dentro do índice dessas frases com o seguinte código:
frase[posição_frase][posição_letra] - (frase[0][0]). Aqui queremos a primeira palavra da frase e sua primeira letra.''')
print(f"Frase: {frase_6}.")
print(frase_6[0][0])









