from datetime import datetime
from datetime import timedelta


# today = datetime.today()
# print(today)
# print(type(today))
#
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.hour)
# print(today.minute)
# print(today.second)
#
# # Форматирование объекта datetime в строку определенного формата
# f_date = today.strftime("%d-%m-%Y %H:%M:%S")
# current_time = today.strftime("%H:%M:%S")
# print(f_date)
# print(current_time)
#
# # Преобразование строки с датой (и временем) в объект datetime
# birth_day = "13.04.1993"
# birth_day_dt = datetime.strptime(birth_day, "%d.%m.%Y")
# print(birth_day_dt, type(birth_day_dt))
# print(birth_day_dt.weekday())
#
# # Арифметические операции с датами
# future_day = today + timedelta(days=5)
# print(future_day)

first_day = "01.01.2025"
second_day = "20.01.2025"

first_day_dt = datetime.strptime(first_day, "%d.%m.%Y")
second_day_dt = datetime.strptime(second_day, "%d.%m.%Y")

delta = second_day_dt - first_day_dt
print(delta.days)