f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")
read = []

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        mark = int(info[6][1:-1])
        read.append(mark)
math_avg = sum(read)/len(read)
print(math_avg)
