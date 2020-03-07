draw_dict = {
    'Россия': 'A',
    'Португалия': 'B',
    'Франция': 'C',
    'Дания': 'C',
    'Египет': 'A'
}
count = 0
for group in draw_dict.values():
    if group == 'C':
        count += 1
# увеличиваем счетчик на 1

# выводим значение счетчика на экран
print(count)
