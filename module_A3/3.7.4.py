f = open("/files/StudentsPerformance.csv")

race = 0
for line in f:
    info = line.split(',')
    ethnicity = info[1][1:-1]
    if ethnicity == 'group C':
        race += 1

print('К этнической группе C относятся:', race, 'студентов')


