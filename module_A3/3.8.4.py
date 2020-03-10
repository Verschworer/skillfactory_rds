f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")

wr = []

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        mark = int(info[7][1:-2])
        wr.append(mark)

wr_ninety = 0
for mark in wr:
    if mark > 90:
        wr_ninety += 1
print(wr_ninety)