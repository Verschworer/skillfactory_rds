# basic_word = input('Введите слово: \n')
# basic_word = 'топот'
basic_word = 'программирование'
inverted_word = basic_word[::-1]
if basic_word == inverted_word:
    print('Слово "'+basic_word+'" является палиндромом')
else:
    print('Слово "'+basic_word+'" - это не палиндром')
