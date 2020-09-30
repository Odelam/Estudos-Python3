def simetrica(m):
    numero_linhas = len(m)
    numero_colunas = len(m[0])

    for i in range(numero_linhas):
        for j in range(i + 1, numero_colunas):
            if m[i][j] != m[j][i]:
                print("Não é simétrica!")
                return False
            else:
                print("É simétrica!")
                return True


m = [[1, 2, 3], [2, 4, 5], [4, 2, 3]]
print(simetrica(m))
