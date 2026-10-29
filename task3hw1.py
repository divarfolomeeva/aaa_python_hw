def orders_analytics():
    orders = [
        {'id': 1, 'buyer': 'anya', 'status': 'delivered', 'amount': 900},
        {'id': 2, 'buyer': 'boris', 'status': 'returned', 'amount': 4_500},
        {'id': 3, 'buyer': 'anya', 'status': 'delivered', 'amount': 1_500},
        {'id': 4, 'buyer': 'vera', 'status': 'delivered', 'amount': 3_200},
        {'id': 5, 'buyer': 'boris', 'status': 'delivered', 'amount': 700},
        {'id': 6, 'buyer': 'gleb', 'status': 'returned', 'amount': 2_100},
    ]

    returned_amount = sum(
        o['amount'] for o in orders if o['status'] == 'returned'
    )
    returned_buyers = {o['buyer'] for o in orders if o['status'] == 'returned'}

    delivered_orders = [o for o in orders if o['status'] == 'delivered']
    delivered_count = len(delivered_orders)
    delivered_amount = sum(o['amount'] for o in delivered_orders)
    avg_delivered_check = (
        delivered_amount / delivered_count if delivered_count else 0
    )

    print(f'сумма оформленных возвратов: {returned_amount}')
    print(f'кто хотя бы раз вернул заказ: {returned_buyers}')
    print(f'сколько заказов доставлено покупателю: {delivered_count}')
    print(f'средний чек доставленных заказов: {avg_delivered_check}')


if __name__ == '__main__':
    orders_analytics()