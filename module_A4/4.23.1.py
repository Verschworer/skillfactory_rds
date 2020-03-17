import re


def count_letters(sentence, average=False):
    if str(average) == 'True':
        pattern = re.compile('\S+')
        list_sentence = pattern.findall(sentence)
        lenght = 0
        words = 0
        for word in list_sentence:
            lenght += len(word)
            words += 1
        result = round(lenght / words, 3)
    else:
        len_sentence = len(sentence.replace(' ', ''))
        result = len_sentence
    return result


print(count_letters("I will build my own theme park"))
print(count_letters("I will build my own theme park", average=True))
