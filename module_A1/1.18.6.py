hour = int (input('Который час: \n'))
#hour = 18
minute = int (input('Сколько минут: \n'))
#minute = 47
if (hour >= 10 and minute < 30) and (hour >= 12 and (hour <= 13 and minute <=40)) and (hour < 18 and (hour > 19 and minute < 30)) and (hour < 20):
    print("Преподаватель свободен.")
else:
    print("Преподаватель занят.")