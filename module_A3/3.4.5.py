name = 'Севастиан'
for letter in name:
    if letter.lower() in ['а', 'о', 'у', 'э', 'я', 'ё', 'ю', 'и', 'е']:
        print(letter, '- гласная буква')
    else:
        print(letter, '- согласная буква')