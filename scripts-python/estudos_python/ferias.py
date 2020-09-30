import datetime


data_atual = datetime.datetime.now().date()
nome_dia_semana = ''
lista_dia_semana = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']

dia_do_mes = int(input("Digite o mês em que irá viajar: "))
while dia_do_mes > 12:
    if dia_do_mes != int:
        print("Mês inválido!")
        print("Informe os meses em números.")
        dia_do_mes = int(input("Digite o mês em que irá viajar: "))

dia_da_semana = input("Digite o dia da semana (seg, ter, qua, qui, sex, sab, dom): ").strip().lower()
while dia_da_semana not in lista_dia_semana:
    if dia_da_semana == 'seg':
        dia_da_semana = 1
        nome_dia_semana = 'Segunda-Feria'
    elif dia_da_semana == 'ter':
        dia_da_semana = 2
        nome_dia_semana = 'Terça-Feira'
    elif dia_da_semana == 'qua':
        dia_da_semana = 3
        nome_dia_semana = 'Quarta-Feira'
    elif dia_da_semana == 'qui':
        dia_da_semana = 4
        nome_dia_semana = 'Quinta-Feira'
    elif dia_da_semana == 'sex':
        dia_da_semana = 5
        nome_dia_semana = 'Sexta-Feira'
    elif dia_da_semana == 'sab':
        dia_da_semana = 6
        nome_dia_semana = 'Sábado'
    elif dia_da_semana == 'dom':
        dia_da_semana = 7
        nome_dia_semana = 'Domingo'
    else:
        print("Dia incorreto!")
    dia_da_semana = input("Digite o dia da semana (seg, ter, qua, qui, sex, sab, dom): ").strip().lower()

numero_dias_de_ferias = int(input("Digite a quantidade de dias das férias: "))
calculo_dias = datetime.date.fromordinal(data_atual.toordinal() + numero_dias_de_ferias)

print("Número de dias de férias", calculo_dias.weekday())

