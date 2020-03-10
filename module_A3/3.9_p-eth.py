students = {}

f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        ethnicity = info[1][1:-1]
        parents = info[2][1:-1]
        if ethnicity in students:
            if parents in students[ethnicity]:
                students[ethnicity][parents] += 1
            else:
                students[ethnicity][parents] = 1
        else:
            students[ethnicity] = {}
            students[ethnicity][parents] = 1
print(students)