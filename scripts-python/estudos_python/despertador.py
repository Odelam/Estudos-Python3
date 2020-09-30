import datetime
import time


def esta_na_hr(hora, minuto, data_atual):
    if data_atual.hour == hora and data_atual.minute == minuto:
        return True
    return False


def processa_dia_semana(dias_semana):
    dias_semana_int = []
    for dia in dias_semana:
        if dia == 'seg':
            dias_semana_int.append(0)
        if dia == 'ter':
            dias_semana_int.append(1)
        if dia == 'qua':
            dias_semana_int.append(2)
        if dia == 'qui':
            dias_semana_int.append(3)
        if dia == 'sex':
            dias_semana_int.append(4)
        if dia == 'sab':
            dias_semana_int.append(5)
        if dia == 'dom':
            dias_semana_int.append(6)
    return dias_semana_int


def esta_no_dia_semana(dias_semana, data_atual):
    if data_atual.weekday() in dias_semana:
        return True
    return False


print("*-" * 20)
print("Despertador")
print("*-" * 20)

hora_str = input("Que horas deseja acordar? (hh:mm): ")
dia_semana_str = input("Qual dia da semana? (Seg; Ter; Qua; Qui, Sex; Sab, Dom): ").lower().strip()

hora = int(hora_str.split(':')[0])
minuto = int(hora_str.split(':')[1])
dias_semana = dia_semana_str.split(' ')
dias_semana_int = processa_dia_semana(dias_semana)

agora = datetime.datetime.now()

cont = 1
while True:
    agora = datetime.datetime.now()
    print(agora)
    if esta_na_hr(hora, minuto, agora) and esta_no_dia_semana(dias_semana_int, agora):
        print("Acordar!")
        if cont >= 3:
            break
    time.sleep(5)
    cont += 1
