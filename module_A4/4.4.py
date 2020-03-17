arr = [5, 2, 1, 3, 4]


def get_median(arr):
    sor_lst = sorted(arr)
    len_lst = len(arr)
    index = (len_lst - 1) // 2
    if (len_lst % 2):
        return sor_lst[index]
    return int(sor_lst[index] + sor_lst[index + 1]) / 2


print(int(get_median(arr)))
