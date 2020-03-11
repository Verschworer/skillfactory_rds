f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")
read = []

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    elif info[0] == '"male"':
        mark = int(info[6][1:-1])
        read.append(mark)
read_avg = sum(read) / len(read)
print(round(read_avg, 3))
