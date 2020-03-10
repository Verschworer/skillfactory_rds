import re

pattern = re.compile('\d+')

exams = []

f = open("/home/verschworer/PycharmProjects/SKILLFACTORY/files/StudentsPerformance.csv")


for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        new_line = []
        for item in info:
            if pattern.search(item) is not None:
                new_line.append(int(pattern.search(item)[0]))
            else:
                new_line.append(item[1:-1])
        exams.append(new_line)
