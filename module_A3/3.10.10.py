f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")

wr = []

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    elif info[3] == '"free/reduced"':
        mark = int(info[7][1:-2])
        wr.append(mark)
wr_avg = sum(wr) / len(wr)
print(round(wr_avg, 2))
