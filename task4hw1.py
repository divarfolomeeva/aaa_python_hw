def shop_stats():
    days = [
        {'day': 'пн', 'orders': 20, 'revenue': 40_000, 'returns': 2},
        {'day': 'вт', 'orders': 16, 'revenue': 19_200, 'returns': 4},
        {'day': 'ср', 'orders': 25, 'revenue': 55_000, 'returns': 1},
        {'day': 'чт', 'orders': 10, 'revenue': 12_000, 'returns': 3},
        {'day': 'пт', 'orders': 30, 'revenue': 48_000, 'returns': 3},
    ]

    total_revenue = sum(d['revenue'] for d in days)
    biggest_revenue_day = max(days, key=lambda d: d['revenue'])['day']

    avg_revenue_per_order = {
        d['day']: d['revenue'] / d['orders'] for d in days
    }
    return_days = [d['day'] for d in days if d['returns'] / d['orders'] > 0.2]

    print(f'выручка за всю неделю: {total_revenue}')
    print(f'день с самой большой выручкой: {biggest_revenue_day}')
    print(
        'средняя выручка на один заказ в каждый день: '
        f'{avg_revenue_per_order}'
    )
    print(f'дни, где возвратов больше 20% заказов: {return_days}')


if __name__ == '__main__':
    shop_stats()