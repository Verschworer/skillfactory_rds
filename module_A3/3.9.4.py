students = {}

f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        ethnicity = info[1][1:-1]
        test = info[4][1:-1]
        if ethnicity in students:
            if test in students[ethnicity]:
                students[ethnicity][test] += 1
            else:
                students[ethnicity][test] = 1
        else:
            students[ethnicity] = {}
            students[ethnicity][test] = 1
print(students)
