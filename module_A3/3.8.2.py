f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")

read = []

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        mark = int(info[6][1:-1])
        read.append(mark)
read_avg = sum(read) / len(read)
below_avg = 0
for mark in read:
    if mark < read_avg:
        below_avg += 1
print(below_avg)