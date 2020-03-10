students = {}

f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        gender = info[0][1:-1]
        test = info[4][1:-1]
        if gender in students:
            if test in students[gender]:
                students[gender][test] += 1
            else:
                students[gender][test] = 1
        else:
            students[gender] = {}
            students[gender][test] = 1
print(students)