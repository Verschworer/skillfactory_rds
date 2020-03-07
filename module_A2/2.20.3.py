defect_stats = [
    {'step number': 1, 'damage': 0.98},
    {'step number': 2, 'damage': 0.99},
    {'step number': 3, 'damage': 0.99},
    {'step number': 4, 'damage': 0.96},
    {'step number': 5, 'damage': 0.97},
    {'step number': 6, 'damage': 0.97},
]
health = 100
for record in defect_stats:
    health *= record['damage']
    if health < 90:
        print('health =', str(health), '&', 'step =', record['step number'])
        break
