word = input('Введите слово: \n')
letter = input('Выбирите букву: \n')
#word = 'ОченьДлинноеСлово'
#letter = 'и'
if (letter in word) == True:
    print('Выбранная буква есть в введённом слове')
else:
    print('Выбранной буквы нет в введённом слове')