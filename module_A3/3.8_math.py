f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")
math = []

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        mark = int(info[5][1:-1])
        math.append(mark)
math_avg = sum(math)/len(math)
above_avg = 0
for mark in math:
    if mark > math_avg:
        above_avg += 1
print(above_avg / 1000)