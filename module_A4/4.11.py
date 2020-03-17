values = [4, 8, 15, 16, 23, 42]
mean = 18
result = filter(lambda x: x > mean, values)
result = list(result)
print(result)