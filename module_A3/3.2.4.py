proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
new_proverb = str()
for i in range(0, len(proverb), 2):
    new_proverb = new_proverb + new_proverb.join(proverb[i + 1])
    new_proverb = new_proverb + new_proverb.join(proverb[i])
print(new_proverb)