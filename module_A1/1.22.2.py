# weight = int(input('Введите вес: \n'))
# weightMAX = int(input('Введите допустимый вес: \n'))
weight = 77
weightMAX = 400
weightover =0

while weightover < weightMAX:
    weightover += weight
print('Перевес ' + str(weightover-weightMAX) + ' кг')