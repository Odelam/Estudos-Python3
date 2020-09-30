import datetime

hora_atual = datetime.datetime.now()
print(hora_atual)

horas = int(input("Informe daqui quantas horas deseja que o alarme soe: "))
hora_despertar = hora_atual + datetime.timedelta(hours=horas)
data_despertar = hora_atual + datetime.timedelta(hours=horas)

hora_despertar = hora_despertar.strftime("%H:%M")  # transforma a hora em um string e nos permite formatar
data_despertar = data_despertar.strftime("%d/%m/%y")
# hora_despertar = str(hora_despertar).split()
# data = hora_despertar[0]
# hora = hora_despertar[1][0:8]
print(f"O relógio irá despertar na data: {data_despertar} e na hora: {hora_despertar}.")

