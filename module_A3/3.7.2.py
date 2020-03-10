import collections

f = open("/files/StudentsPerformance.csv")

c = collections.Counter()

education = []
for line in f:
    info = line.split(',')
    education.append(info[2][1:-1])
    for word in education:
        c[word] += 1
print(len(c) - 1)
