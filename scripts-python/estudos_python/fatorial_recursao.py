def fatorial(n):
    if n == 0:
        return 1
    else:
        resultado = n * fatorial(n - 1)
        return resultado


print(fatorial(7))