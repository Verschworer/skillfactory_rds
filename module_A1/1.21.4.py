number = int(input('Введите число: \n'))
# number = 173
for i in range(1, number + 1, 1):
    if number % i == 0 and i != 1 and i != number:
        print('Не является простым')
        break
else:
    print('Простое')