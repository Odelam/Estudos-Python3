print('''
Suponha que queremos definir uma função que calcula f(x):
f(x) = x² + 1
Podemos definir a função como: 
''')


def funcao(x):
    resposta = x ** 2 + 1
    print(f"Função de {x} é: {resposta}.")
    return resposta


def juros(preco, juros):
    resposta = preco * (1 + (juros / 100))
    print(f"O valor de {preco:.2f} com juros atualizado, é: {resposta:.2f}.")
    return resposta


def f(x):
    """Exemplo de documentação de funções que será impresso por meio da função help()"""
    res = x ** x + 1
    return res


funcao(4)
juros(10, 50)
help(f)
