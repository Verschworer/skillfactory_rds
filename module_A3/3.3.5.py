emails_list = ['vasya@mail.ru',
               'akakiy@yandex.ru',
               'spyderman@yandex.ru',
               'XFiles@gmail.com',
               'hello@mail.ru',
               'noname@gmail.com',
               'DonaldTrump@mail.ru',
               'a768#af@yandex.ru',
               'Ivan_Ivanovich@yandex.ru',
               'thebestmail@yandex.ru']
emails_dict = {}
for email in emails_list:
    domain = email[(email.find(r'@') + 1):]
    if domain in emails_dict:
        emails_dict[domain] += 1
    else:
        emails_dict[domain] = 1
print(emails_dict)
