import time

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


n = 35

start = time.time()
print(finobacci_recursao(n))
print(f"Função recursiva, tempo de execusão: {time.time() - start} segundos") # 3.264035224914551
print()

start = time.time()
print(finobacci_iteracao(n))
print(f"Função iteração, tempo de execusão: {time.time() - start} segundos") # 6.222724914550781e-05