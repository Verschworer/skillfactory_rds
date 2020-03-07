draw_dict = {
    'Россия': 'A',
    'Португалия': 'B',
    'Франция': 'C',
    'Дания': 'C',
    'Египет': 'A'
}

# country = input('Введите интересующие страны: \n')
# request = country.split(' ')
# print(request)
request = ['Италия']
for country in request:
    if country in draw_dict:
        group = (draw_dict[country])
        print(group)
    else:
        group = ('unknown')
        print(group)