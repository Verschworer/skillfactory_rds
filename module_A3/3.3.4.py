number = 56.257
num = str(number)
pos = num.find('.')
print(int(num[pos + 1]) + int(num[pos + 2]) + int(num[pos + 3]))