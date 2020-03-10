students = {}

f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        gender = info[0][1:-1]
        p_l_education = info[2][1:-1]
        if gender in students:
            if p_l_education in students[gender]:
                students[gender][p_l_education] += 1
            else:
                students[gender][p_l_education] = 1
        else:
            students[gender] = {}
            students[gender][p_l_education] = 1

print(students)
