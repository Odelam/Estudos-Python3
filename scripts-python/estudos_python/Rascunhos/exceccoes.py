def divide(divide_por):
    try:
        return 42 / divide_por
    except ZeroDivisionError:
        print('Erro: Número inválido!')

for i in range(5):
    print(divide(i))