from collections import Counter


def queries_analytics():
    queries = [
        'чехол',
        'iphone',
        'чехол',
        'наушники',
        'iphone',
        'iphone',
        'кабель',
        'чехол',
        'iphone',
    ]

    queries_total = len(queries)
    query_count = Counter(queries)

    most_common_count = max(query_count.values())
    most_common_query = None

    for query, count in query_count.items():
        if count == most_common_count:
            most_common_query = query
            break

    share = round((most_common_count / queries_total) * 100, 2)
    unique_queries = [q for q, count in query_count.items() if count == 1]

    print(f'всего поисковых запросов в ленте: {queries_total}')
    print(f'сколько раз ввели каждый запрос: {dict(query_count)}')
    print(f'какой запрос вводили чаще всего: {most_common_query}')
    print(f'какую долю поисков он занимает: {share}%')
    print(f'какие запросы встретились один раз: {unique_queries}')


if __name__ == '__main__':
    queries_analytics()