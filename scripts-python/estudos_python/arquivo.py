def ler_arquivo(nome_do_arquivo):
    arquivo = open(nome_do_arquivo, 'r')
    conteudo = arquivo.read()
    arquivo.close()
    lista_de_palavras = conteudo.split()
    print(lista_de_palavras)
    return len(lista_de_palavras), len(conteudo)


palavras, caracteres = ler_arquivo('nomes_pessoas.txt')
print('Quantidade de palavras no arquivo: ', palavras)
print('Quantidade de caracteres no arquivo: ', caracteres)
