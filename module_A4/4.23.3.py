def always(n):
    def num(value=n):
        return value

    return num


print(always(8))
