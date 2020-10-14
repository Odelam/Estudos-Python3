numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    numero = int(input("Digite um número entre 0 e 10: "))
    if numero >= 0 and numero <= 10:
        break
    print("Número fora do range.", end=' ')

for p, n in enumerate(numeros_extenso):
    if p == numero:
        print(f'Você digitou o número: {n.title()}.')


