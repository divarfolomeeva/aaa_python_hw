def warehouses():
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}
    both_cities = moscow & kazan
    only_moscow = moscow - kazan
    only_kazan = kazan - moscow
    total_items = len(moscow | kazan)

    print(f'можно забрать в любом из двух городов: {both_cities}')
    print(f'можно забрать только в Москве: {only_moscow}')
    print(f'можно забрать только в Казани: {only_kazan}')
    print(f'всего товаров на складах: {total_items}')


if __name__ == '__main__':
    warehouses()
