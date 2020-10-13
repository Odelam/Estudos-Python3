numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

numero = int(input("Digite um número entre 0 e 10: "))
while numero > len(numeros_extenso) or numero < 0:
    print('Número fora do range! Digite novamente.')
    numero = (input("Digite um número entre 0 e 10: "))

for p, n in enumerate(numeros_extenso):
    if p == numero:
        print(f'Você digitou o número: {n}.')
        break

