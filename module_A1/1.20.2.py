# number = int(input()) #консольный ввод
number = 84
for i in range(1, number + 1, 1):
    if number % i == 0 and number % i != number:
        print(i)
