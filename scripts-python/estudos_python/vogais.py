lista_palavras = ('felinos', 'caçadores', 'solitarios', 'ageis', 'noturnos', 'mortais', 'adaptaveis')
vogais = []


for palavra in lista_palavras:
    cont = 0
    for v in palavra:
        if v in 'aeiou':
            vogais.append(v)
    if cont <= len(lista_palavras):
        print(palavra, vogais)
        cont += 1