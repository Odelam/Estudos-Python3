def fatorial(n):
    if n == 0:
        return 1
    else:
        resultado = n * fatorial(n - 1)
        return resultado


# l = [1, 2, (3, 4)]
# print(l)
# print(l[0])
# print(l[2])
# print(l[2][0])
# print(l[-1][0])
#
# x, y = 2, 3
# print('x', x)
# print('y', y)
# print()
#
# y, x = x, y
# print('x', x)
# print('y', y)
#
# class Ponto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p = Ponto(1, 2)
# q = Ponto(3, 4)
#
# print(f"p: {p.x,y}")
# print(f"q: {q.x,y}")

# class Ponto:
#     x = 0
#     y = 0
#
# p = Ponto()
# Ponto.x = 1
# p.x = 2
# p.y = 3
# Ponto.y = 4
# print(f"Ponto.x:{Ponto.x}")
# print(f"p.x:{p.x}")
# print()
# print(f"Ponto.y:{Ponto.y}")
# print(f"p.y:{p.y}")

class Cachorro:
    def __init__(self, idade):
        self.idade = idade


class Dalmata(Cachorro):
    def __init__(self, idade, pedigree):
        super(Dalmata, self).__init__(idade)
        self.pedigree = pedigree

d = Dalmata(3, True)
print(d.idade, d.pedigree)