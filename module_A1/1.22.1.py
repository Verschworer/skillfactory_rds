#Y = int(input('Введите начальную сумму средств: \n'))
#Z = int(input('Введите требуемую сумму средств: \n'))
Y = 170000
Z = 1000000
years = 0
multiplier = 1.1

while Y < Z:
    Y = Y*multiplier
    years += 1
else:
    print(years)