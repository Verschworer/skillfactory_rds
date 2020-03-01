# num_1 = int (input('Введите число: \n'))
num_1 = 1812
# num_2 = int (input('Введите еще число: \n'))
num_2 = 2500
if num_1 < num_2:
    for i in range(num_1, 1, -1):
        if num_1 % i == num_2 % i == 0:
            print(i)
            break
    else:
        print("Общих делителей не найдено")
else:
    for i in range(num_2, 1, -1):
        if num_1 % i == num_2 % i == 0:
            print(i)
            break
    else:
        print("Общих делителей не найдено")
