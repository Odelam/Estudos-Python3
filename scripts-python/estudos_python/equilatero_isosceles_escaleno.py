

print("-=-*" * 20)
print("Analisador de Triângulos.")
print("*-=-" * 20)

r1 = float(input("Digite o valor da reta: "))
r2 = float(input("Digite o valor da reta: "))
r3 = float(input("Digite o valor da reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print(f"Os segmentos formam um triângulo.")
    if r1 == r2 and r2 == r3 and r3 == r1:
        print("Equilátero.")
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print("Isósceles.")
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print("Escaleno.")
else:
    print("Segmentos não formam um triângulo.")


# outra maneira de fazer

a = eval(input("Digite o valor da reta: "))
b = eval(input("Digite o valor da reta: "))
c = eval(input("Digite o valor da reta: "))

maior_lado = 0

# if a > maior_lado:
#     a = maior_lado
# if b > maior_lado:
#     b = maior_lado
# if c > maior_lado:
#     c = maior_lado

maior_lado = max(a, b, c)

if maior_lado < a + b + c - maior_lado:
    print("Os lados formam um triângulo!")
    if a == b and b == c and a == c:
        print("Equilátero!")
    elif a != b and b != c and a != c:
        print("Escaleno!")
    elif a == b or b == c or a == c:
        print("Isóseles!")
else:
    print("Os lados não formam um triângulo.")
