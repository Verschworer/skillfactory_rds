import numpy as np
user_db = [{'orders': 12}, {'orders': 30}, {'orders': 45}]


def avg_orders(user_db):
    order_sum = []
    for user in user_db:
        order_sum.append(user['orders'])
    orders_per_user = np.mean(order_sum)
    return orders_per_user


opu = avg_orders(user_db)
print(opu)
