m = dict()


def fatorial(n):
    if n == 0:
        return 1
    elif m.get(n) is not None:
        return m[n]
    else:
        m[n] = n * fatorial(n - 1)
        return m[n]


n = 20
print(fatorial(n))
