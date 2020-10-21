class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return self.x, self.y

    def mover(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        return f'{self.x}, {self.y}'

    # x + y -> (2, 2) + (2, 1) => (4, 3)
    # x + y -> (2, 2) + 8 => (10, 10)
    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.x + other)


ponteiro = Point()
ponteiro.setx(5)
ponteiro.sety(3)

ponteiro_1 = Point()
ponteiro_1.setx(2)
ponteiro_1.sety(2)

novo_ponto = ponteiro + ponteiro_1

ponteiro_2 = Point()
ponteiro_2.sety(3)
ponteiro_2.setx(3)
novo_ponto_2 = ponteiro_2 + 2

print(f"({novo_ponto})")
print(f'({ponteiro_2})')
