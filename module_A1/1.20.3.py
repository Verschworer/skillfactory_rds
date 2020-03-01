# num_1 = int (input('Введите число: \n'))
num_1 = 12
# num_2 = int (input('Введите еще число: \n'))
num_2 = 38

for i in range(1, num_1 + 1, 1):
    if num_1 % i == 0 and num_2 % i == 0 and i != 1:
        print(i)
