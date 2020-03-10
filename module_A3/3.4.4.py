string = 'Тяжёлая интернет-зависимость - это когда ты выходишь из интернета, а он из тебя нет.'
for i in string:
    if i == '.' or i == ',' or i == '-' or i == ':' or i == '!' or i == '?':
        string = string.replace(i, ':)')
print(string)
