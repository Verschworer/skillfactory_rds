number = int (input('Введите число: \n'))
#number = 346
if number%2 == 0 or number%5 == 0 or number%173 == 0 or number%821 == 0:
    print("Вова, это нужное число")
else:
    print("Вова, в этот раз ты не попал")