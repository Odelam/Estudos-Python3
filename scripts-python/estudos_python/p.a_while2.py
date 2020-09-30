escolha = ''
while escolha != 'S':
    primeiro = int(input("Primeiro termo: "))
    razao = int(input("Razão da P.A: "))
    termo = primeiro
    cont = 1
    total = 0
    mais = 10
    while mais != 0:
        total = total + mais
        while cont <= total:
            print(f"{termo}", end='')
            if cont < total:
                print(" -> ", end='')
            else:
                print(".")
            termo += razao
            cont += 1
        print("Pausa...")
        mais = int(input("Quantos termos vc ainda quer mostrar: "))
        if mais == 0:
            print("Tem certeza que deseja encerrar?")
            escolha = str(input("[S] - Sim; [N] - Não: ")).strip().upper()

print('fim.')
