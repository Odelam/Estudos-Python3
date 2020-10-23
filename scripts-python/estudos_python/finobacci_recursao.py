def finobacci_recursao(n):
    if n < 2:
        return n
    else:
        return finobacci_recursao(n - 1) + finobacci_recursao(n - 2)


def finobacci_iteracao(n):
    resultado = n
    a, b = 0, 1
    for k in range(2, n + 1):
        resultado = a + b
        a, b = b, resultado
    return resultado


print('Recursão', finobacci_recursao(6))
print('Iteração', finobacci_iteracao(6))
