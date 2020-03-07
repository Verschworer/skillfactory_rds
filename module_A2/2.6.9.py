raw_list = ['переменные', 'циклы', 'условия', 'списки', 'словари', 'файлы', 'функции']
my_list = []
for word in raw_list:
    my_list.append(len(word))
result = min(my_list) + max(my_list)
print(result)
