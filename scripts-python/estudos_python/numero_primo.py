
for c in range(1, 4):
    num = int(input("Digite um número e descubra se é primo: "))
    if num % 2 != 0 or num == 2:
        print(f"O número {num} é primo.")
    elif num == 1:
        print(f"O número {num} não é primo.")
    else:
        print(f"O número {num} não é primo.")
print("Fim")

# de uma outra maneira
num = int(input("Digite um número: "))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end="")
        total += 1
    else:
        print("\033[31m", end="")
    print(f"{c}", end="")
print(f"\033[m O número {num} foi divisível {total} vezes.")
if total == 2:
    print("É primo!")
else:
    print("Não é primo!")
