# List of orders
orders = [
    {'id': 1, 'products': [
        {'productId': 1, 'quantity': 3},
        {'productId': 2, 'quantity': 2},
    ]},
    {'id': 2, 'products': [
        {'productId': 1, 'quantity': 3},
        {'productId': 5, 'quantity': 2},
    ]},
    {'id': 3, 'products': [
        {'productId': 1, 'quantity': 3},
        {'productId': 3, 'quantity': 2},
        {'productId': 4, 'quantity': 1},
    ]},
]


def get_all_orders():
    return orders
