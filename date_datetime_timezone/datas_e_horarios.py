# Python datetime: Lidando com datas e horários

from datetime import date, datetime

# Formatando nossa data em uma string:

actual_day = date.today()
print(f'Padrão ANSI: {actual_day}')
print(f'Padrão brasileiro: {actual_day.day}/{actual_day.month}/{actual_day.year}')

#Formatando datas em strings usando o método strftime()

usando_strftime = actual_day.strftime('%d/%m/%y')
print(f'Padrão brasileiro, usando o strftime: {usando_strftime}')
print()

# Pegando data e hora atual:
pegando_data_e_hora = datetime.now()
data_hora_e_texto = pegando_data_e_hora.strftime('%d/%m/%y - %H:%M:%S')
print(f'Pegando data e hora atual:: {data_hora_e_texto}')
