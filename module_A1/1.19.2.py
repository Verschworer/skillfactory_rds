#year_1 = (input('Ввелите начальный год: \n'))
#year_2 = (input('Ввелите конечный год: \n'))
year_1 = 2013
year_2 = 2020
for i in range(year_1, year_2+1, 1):
    if i%4 == 0:
        print(str(i)+' год високосный')
    else:
        print(str(i)+' год невисокосный')