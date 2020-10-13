print('*' * 20)
print('{:^20}'. format('Banco'))
print('*' * 20)

valor = int(input("Qual valor deseja sacar? R$:"))
total = valor
cedula = 200
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}.')
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1

        total_cedula = 0
        if total == 0:
            break

print("Fim!")