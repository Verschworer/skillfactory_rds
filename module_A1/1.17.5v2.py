#number = int (input('Ввелите число: \n'))
number = 11
if number%2 == 0:
    print("Число делится на 2 без остатка.")
elif number%3 == 0:
    print("Число делится на 3 без остатка.")
elif number%5 == 0:
    print("Число делится на 5 без остатка.")
else:
    print("Число не делится ни на 2, ни на 3, ни на 5 без остатка!")