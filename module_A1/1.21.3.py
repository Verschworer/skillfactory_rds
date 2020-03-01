for i in range(5):
    string = (input('Любите ли вы Python? \n'))
    # string = 'Нет'
    i = i + 1
    if string == 'да' or string == 'Да' or string == 'ДА':
        print("Это отлично!", )
        break
    elif string == 'нет' or string == 'Нет' or string == 'НЕТ':
        print("Увы, это неправильный ответ")
else:
    print("Это безнадёжно!")
