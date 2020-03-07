draw_dict = {
    'Россия': 'A',
    'Португалия': 'B',
    'Франция': 'C',
    'Дания': 'C',
    'Египет': 'A'
}
draw_new = {}
for country in draw_dict:
    if draw_dict[country] == 'A':
        draw_new[country] = draw_dict[country]
print(draw_new)
