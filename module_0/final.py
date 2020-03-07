import numpy as np
# вводим числа
a = int(input('Введите от: \n'))
b = int(input('Введите до: \n'))
# возможность ввести два любых числа
if a > b:
    a, b = b, a

# загадали число
number = np.random.randint(a, b)
print('Загадано число от', a, 'до', b)


def game_1(number, mid=a+b // 2, low=a, high=b):
    """бинарный поиск"""
    count = 0
    # цикл пока средний среднее среднее число интервала не равно загадонному
    while mid != number:
        # +попытка
        count += 1
        # если загаданное число больше то нижняя граница сдвигается на позицию среднего+1 значения
        # т.к. среднее уже проверенно
        if number > mid:
            low = mid + 1
        # в противном случае сдвигаем верхниюю границу ниже среднего значения
        elif number < mid:
            high = mid - 1
        mid = (low + high) // 2
    # продалжаем сжимать
    return count


def score_game(game_1):
    """Запускаем много раз, чтоб узнать как быстро угадывает число"""
    count_ls = []
    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)
    # побольше повторений для точности
    random_array = np.random.randint(a, b + 1, size=100000)
    for number in random_array:
        count_ls.append(game_1(number))
    # округление
    score = round(float(np.mean(count_ls)))
    # вывод округленного и нет значений
    print(f"Ваш алгоритм угадывает число в среднем за {score} ({np.mean(count_ls)}) попыток")
    return score


# поехали!
score_game(game_1)
