import numpy as np
# вводим числа
a = int(input('Введите от: \n'))
b = int(input('Введите до: \n'))
# возможность ввести два любых числа
if a > b:
    a, b = b, a

# создание массива
rng = []
# заполнение массива
for i in range(a, b+1):
    rng.append(i)

# загадали число
number = np.random.randint(a, b)
print('Загадано число от', a, 'до', b)


def game_1(number, mid=len(rng) // 2, low=0, high=len(rng)):
    """бинарный поиск"""
    count = 0
    # цикл пока средний индекс не равен загадонному числу
    while rng[mid] != number:
        # +попытка
        count += 1
        # если загаданное число больше то нижний индекс сдвигается на позицию средний+1
        # т.к. значение среднего уже проверенно
        if number > rng[mid]:
            low = mid + 1
        # в противном случае сдвигаем верхний индекс ниже среднего
        elif number < rng[mid]:
            high = mid - 1
        mid = (low + high) // 2
    # продалжаем сжимать
    return count


def score_game(game_1):
    """Запускаем игру много раз, чтоб узнать как быстро игра угадывает число"""
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
