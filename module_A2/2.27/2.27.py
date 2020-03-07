import json
import collections

with open('/home/verschworer/PycharmProjects/SKILLFACTORY/module_A2/2.27/data.json', 'rb') as infile:
    data = json.load(infile)

data_list = data['events_data']

categories = []
for item in data_list:
    category = item['category']
    categories.append(category)
# print(categories)

c = collections.Counter()
for category in categories:
    c[category] += 1
# print(c)

table_clients = []
for item in data_list:
    client_id = item['client_id']
    category = item['category']
    if category == 'report':
        table_clients.append(client_id)
print (table_clients)

c = collections.Counter()
for table_client in table_clients:
    c[table_client] += 1
print(c)
print(len(c.keys()))
print(c[62602])