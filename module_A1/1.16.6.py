number = int (input('Введите число: \n'))
#number = 169

if number**(1/2) != int:
    print(int(number**(1/2)))
else:
    print('Квадратный корень из ' +str(number)+' не целое число')