#num_1 = int (input('Введите число: \n'))
num_1 = 25
#num_2 = int (input('Введите еще число: \n'))
num_2 = 45
if num_1 < 0 or num_2 < num_1:
    print("Введён неверный диапазон чисел")
else:
    for i in range(num_1, num_2+1, 2):
        if i%3 == 0 or i%5 == 0:
            print(i)

