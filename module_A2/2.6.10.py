raw_list = [2, 8, 10, 23, 64, 49, 11, 52, 71, 14]
x_min=min(raw_list)
x_max=max(raw_list)
my_list = []

for i in raw_list:
    if i%2==0:
        my_list.append(i*x_min)
    elif i%2!=0:
        my_list.append((i*x_max))
result = max(my_list)
print(result)