
num = float(input("Digite um valor em metros: "))

centimetros = num / 100
milimetro = num * 1000
km = num / 1000
micrometro = num * 1
milha = num / 0.000621371
jarda = num * 1.094
peh = num * 3.281
polegada = num * 39.37
milha_nautica = num / 1852

print(f"Em Centímetros: {centimetros:.2f}!")
print(f"Em Milímetro: {milimetro:.2f}!")
print(f"Em Km: {km}!")
print(f"Em Micrômetro: {micrometro:.2f}!")
print(f"Em Milha: {milha:.2f}!")
print(f"Em Jardas: {jarda:.2f}!")
print(f"Em Pés: {peh:.2f}!")
print(f"Em Polegadas: {polegada:.2f}!")
print(f"Em Milha-Nautica: {milha_nautica:.5f}!")

