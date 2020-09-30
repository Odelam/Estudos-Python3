seguntos = int(input("Digite o números de segundos que deseja converter: "))
horas = seguntos // 3600
segs_restantes = seguntos % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60
print(f"Horas: {horas}, Minutos: {minutos}, Segundos: {segs_restantes_final}.")
