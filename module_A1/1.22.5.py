volume = 1000
water = 5
times = 0
while volume > 0:
    times += 1
    volume -= water * times
    continue
print(times)