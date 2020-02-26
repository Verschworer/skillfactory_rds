weight = int (input('Введите вес, кг: \n'))
#weight = 92
height = int (input('Введите рост, см: \n'))
#height = 180
color = (input('Введите любимый цвет: \n'))
#color = 'синий'
if weight < 80 and height > 170 and color == 'красный':
    print("Ваша половинка нашлась!")
else:
    print("Попробуем поискать ещё...")