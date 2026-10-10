from collections import defaultdict


def task_reviews():
    reviews = [
        {'id': 1, 'product': 'Чехол', 'stars': 5},
        {'id': 1, 'product': 'чехол', 'stars': 3},
        {'id': 1, 'product': 'чехол', 'stars': 4},
        {'id': 2, 'product': 'Наушники', 'stars': 2},
        {'id': 2, 'product': 'наушники', 'stars': 2},
        {'id': 2, 'product': 'НАУШНИКИ', 'stars': 5},
        {'id': 3, 'product': 'Планшет', 'stars': 5},
        {'id': 4, 'product': 'Колонка', 'stars': 4},
        {'id': 4, 'product': 'колонка', 'stars': 4},
        {'id': 5, 'product': 'Кабель', 'stars': 1},
    ]

    product_reviews = defaultdict(list)  # привела названия к одному формату
    for i in reviews:
        product_reviews[i['product'].lower()].append(i['stars'])

    avg_rating = {  # средняя оценка каждого товара
        product: sum(stars) / len(stars)
        for product, stars in product_reviews.items()
    }

    multiple_reviews_products = {
        product: avg
        for product, avg in avg_rating.items()
        if len(product_reviews[product]) >= 2
    }

    worst_product = min(
        multiple_reviews_products,
        key=lambda p: multiple_reviews_products[p]
    )

    low_rating_count = sum(
        1 for review in reviews if review['stars'] in (1, 2)
    )

    reviews_total = len(reviews)
    share_low_rating = round(low_rating_count / reviews_total * 100, 2)

    print(f'средняя оценка каждого товара: {avg_rating}')
    print(
        'худший товар по средней оценке среди тех, '
        f'у кого хотя бы два отзыва: {worst_product}'
    )
    print(f'сколько отзывов на 1 или 2 звезды: {low_rating_count}')
    print(f'какую долю отзывов они составляют: {share_low_rating}%')


if __name__ == '__main__':
    task_reviews()