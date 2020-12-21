from itertools import groupby


order_list = [{"id": "1", "price": 0.5}, {"id": "1", "price": 1.0}, {"id": "2", "price": 1.5 }]


def avg(x):
    return sum(x) / len(x)


def get_stat_for_orders(orders):
    seq = [x["price"] for x in orders]
    min_price = min(seq)
    max_price = max(seq)
    total_price = sum(seq)

    groups = []
    unique_keys = []

    for key, group in groupby(sorted(orders, key=lambda x: x["id"]), lambda x: x["id"]):
        groups.append([item["price"] for item in group])
        unique_keys.append(key)

    avg_price_distrib = dict(map(lambda kv: (kv[0], avg(kv[1])), {i:j for i, j in zip(unique_keys, groups)}.items()))

    return min_price, max_price, avg_price_distrib, total_price


if __name__ == "__main__":
    print(get_stat_for_orders(order_list))
