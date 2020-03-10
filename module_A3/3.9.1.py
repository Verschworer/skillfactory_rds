students = {}
f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        gender = info[0][1:-1]
        lunch = info[3][1:-1]
        if gender in students:
            if lunch in students[gender]:
                students[gender][lunch] += 1
            else:
                students[gender][lunch] = 1
        else:
            students[gender] = {}
            students[gender][lunch] = 1
print(students)
