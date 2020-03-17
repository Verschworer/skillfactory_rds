numbers = []
for i in range(100, 1000, 33):
    numbers.append(i)


def normalize(numbers, mean = 0, std =1):
    nrm = list(map(lambda n: (n - mean)/std, numbers))
    return nrm


print(normalize(numbers))
