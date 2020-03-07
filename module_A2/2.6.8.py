list=[]
result = 0
for i in range (1, 51):
    if i%3==0:
        list.append(i)
        result += i
print(result)