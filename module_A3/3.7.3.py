f = open("/files/StudentsPerformance.csv")

havelunch = 0
for line in f:
    info = line.split(',')
    lunch = info[3][1:-1]
    if lunch == 'standard':
        havelunch += 1

print('Пообедали:', (havelunch * 100) / 1000, '%')
