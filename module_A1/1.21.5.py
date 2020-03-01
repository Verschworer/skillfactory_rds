string = (input('введите фразу: \n'))
# string = 'прелестная строка'
for i, letter in enumerate(string):
    if letter in ['а', 'о', 'у', 'э', 'я', 'ё', 'ю', 'и', 'е'] and i in range(1, len(string) + 1, 2):
        print('Строка мне не нравится!')
        break
else:
    print("Какая хорошая строка!")
