draw_dict = {
    'Россия': 'A',
    'Португалия': 'B',
    'Франция': 'C',
    'Дания': 'C',
    'Египет': 'A'
}
draw_new = {}
for country, group in draw_dict.items():
    if group == 'A':
       # print(country)
        draw_new[country] = draw_dict[country]
print(draw_new)