f = open("/files/StudentsPerformance.csv")

bachelor = 0
for line in f:
    info = line.split(',')
    parental_level_of_education = info[2][1:-1]
    if parental_level_of_education == "bachelor's degree":
        bachelor += 1

print('Бакалавров:', bachelor)