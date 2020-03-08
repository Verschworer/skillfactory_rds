from termcolor import colored

currency = {'AMD': {
    'Name': 'Армянских драмов',
    'Nominal': 100,
    'Value': 13.121
}, 'AUD': {
    'Name': 'Австралийский доллар',
    'Nominal': 1,
    'Value': 45.5309
}, 'INR': {
    'Name': 'Индийских рупий',
    'Nominal': 100,
    'Value': 92.9658
}, 'MDL': {
    'Name': 'Молдавских леев',
    'Nominal': 10,
    'Value': 36.9305
}}

cur = {}
for record in currency.items():
    cur.setdefault(record[0], (record[1]['Value'] / record[1]['Nominal']))
for record in cur:
    if record is min(cur.keys()):
        print(colored(record, 'red',), end=' ')
    else:
        print(record, end=' ')
