def raiz_quadrada(n):
    return n ** 2


print(raiz_quadrada(3))


def raizquadrada(n):
    root = n / 2
    for c in range(20):
        root = (1 / 2) * (root + (n / root))
    return root


print(f"{raizquadrada(12):.2f}")
