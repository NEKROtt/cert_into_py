# Задача 2. Работа с текущим временем и датой Напишите скрипт, 
# который получает текущее время и дату, а затем выводит их в формате YYYY-MM-DD HH:MM:SS. 
# Дополнительно, выведите день недели и номер недели в году.


from datetime import datetime

date_time_now = datetime.now()
print(date_time_now)

string_date_time = datetime.strftime(date_time_now, "%Y-%m-%d  %H:%M:%S")
print(string_date_time)

day_of_week = date_time_now.strftime("%A")
print(day_of_week)

num_week = date_time_now.isocalendar()[1]
print(num_week)