m = dict()


def fibonacci(n):
    if n < 2:
        return n
    elif m.get(n) is not None:
        return m[n]
    else:
        m[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return m[n]


n = 20
print(fibonacci(n))
