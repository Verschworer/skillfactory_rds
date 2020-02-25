mark = int (input('Введите отметку: \n'))
#mark = 7
if mark < 4:
    print('неудовлетворительно')
elif 4 <= mark < 6:
    print('удовлетворительно')
elif 6 <= mark <= 7:
    print('хорошо')
else:
    print("отлично")