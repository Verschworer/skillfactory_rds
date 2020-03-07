draw_dict = {
    'Россия': 'A',
    'Португалия': 'B',
    'Франция': 'C',
    'Дания': 'C',
    'Египет': 'A'
}
# country = input('Введите интересующие страны: \n')
country = 'Италия'
if country not in draw_dict:
    group = 'unknown'
    draw_dict.setdefault(country, group)
    print(country, group)
print(draw_dict)
