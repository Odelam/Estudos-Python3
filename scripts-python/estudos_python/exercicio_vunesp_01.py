a = [1, 2, 3]
b = a
b[1] = 4

if a == b:
    print("A")
else:
    print("B")
a = (4, 5, 6)
b[1] = 7
if a == b:
    print("C")
else:
    print("D")
