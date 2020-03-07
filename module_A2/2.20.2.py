results = [
    {'cost': 98, 'source': 'vk'},
    {'cost': 153, 'source': 'yandex'},
    {'cost': 110, 'source': 'facebook'},
]
cost_min = []
for record in results:
    cost_min.append(record['cost'])
print(min(cost_min))
