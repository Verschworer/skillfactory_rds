#n = int (input('Введите число: \n'))
n = 10
k=0
fib=0
for  i in range (1, n+1):
    fib=i+k
    i=k
    k=fib
print(fib)

