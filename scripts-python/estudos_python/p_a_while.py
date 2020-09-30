primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da P.A: "))
termo = primeiro
cont = 1

while cont <= 10:
    print(f"{termo}", end='')
    if cont < 10:
        print(" -> ", end='')
    else:
        print(".")
    termo += razao
    cont += 1
