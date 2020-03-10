students = {}
f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        ethnicity = info[1][1:-1]
        if ethnicity in students:
            students[ethnicity] += 1
        else:
            students[ethnicity] = 1
print(students)