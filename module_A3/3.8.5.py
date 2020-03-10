f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")

lunch_standard = []
lunch_any = []

for line in f:
    info = line.split(',')
    lunch = info[3][1:-1]
    if info[0] == '"gender"':
        continue
    elif lunch == 'standard':
        mark = int(info[7][1:-2])
        lunch_standard.append(mark)
    else:
        mark = int(info[7][1:-2])
        lunch_any.append(mark)

lunch_std_ninety = 0
lunch_any_ninety = 0

for mark in lunch_standard:
    if mark > 90:
        lunch_std_ninety += 1
        lunch_any_ninety += 1

for mark in lunch_any:
    if mark > 90:
        lunch_any_ninety += 1

print('Стандартно питаются', round((lunch_std_ninety * 100 / lunch_any_ninety), 1), '% студентов, получивших за '
                                                                                    'экзамен по письму выше 90 баллов')
