import collections
f = open("/files/StudentsPerformance.csv")
c = collections.Counter()
race = []
for line in f:
    info = line.split(',')
    race.append(info[1][1:-1])
    for word in race:
        c[word] += 1

print('Этнических групп:', (len(c) - 1))

