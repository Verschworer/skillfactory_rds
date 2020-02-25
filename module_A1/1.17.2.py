#weight = float (input('Введите вес, кг: \n'))
weight = 80
#height = float (input('Введите рост, м: \n'))
height = 1.8
if weight/height**2 < 18.5:
    print("Недостаточная масса тела")
elif weight/height**2 > 24.99:
    print("Избыточная масса тела")
else:
    print("Норма")


#print("ИМТ = "+ str(weight/height**2))