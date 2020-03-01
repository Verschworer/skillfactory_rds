# string = (input('введите фразу: \n'))
string = 'абстракция'
for i, letter in enumerate(string):
    if letter == 'а' or letter == 'б' or letter == 'в':
        continue
    print(letter, end='')
