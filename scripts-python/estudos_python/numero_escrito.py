numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
resposta = ' '

while resposta != 'N':
    while True:
        numero = int(input("Digite um número entre 0 e 10: "))
        if 0 <= numero <= 10:
            break
        print("Número fora do range.", end=' ')

    for p, n in enumerate(numeros_extenso):
        if p == numero:
            print(f'Você digitou o número: {n.title()}.')

    resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if resposta == 'N':
        print()
        print("Até mais!")
        break


