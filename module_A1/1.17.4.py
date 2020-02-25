#balance = int (input('Введите отметку: \n'))
balance = 455
if balance < 2500:
    print("Придётся потерпеть!")
elif 2500 <= balance <= 5000:
    print("Эх, только фастфуд.")
else:
    print("Сегодня твой выбор - ресторан!")