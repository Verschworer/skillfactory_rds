def get_euro_rate():
    import random
    return random.randrange(65, 85)


def to_euro(price):
    exchange_rate = get_euro_rate()
    rounded = round(price / exchange_rate, 2)
    return '€' + str(rounded)


print(to_euro(200))
