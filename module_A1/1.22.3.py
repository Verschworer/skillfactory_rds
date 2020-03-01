# current_health = int(input('Введите текущее HP: \n'))
# attack = int(input('Введите DPS врага: \n'))
current_health = 500
attack = 80
time =0

while current_health > 0:
    current_health = current_health - attack
    time += 1
print(time)