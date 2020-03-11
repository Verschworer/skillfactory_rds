f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")

read = []
math = []

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        mark = int(info[5][1:-1])
        math.append(mark)
        max_math = max(math)
        print(math)
        for line in f:
            info = line.split(',')
            mark_r = info[6][1:-1]
            if info[0] == '"gender"':
                continue
            elif int(info[5][1:-1]) == 100:
                mark_r = int(info[6][1:-1])
                read.append(mark_r)
