

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_price_map = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }

    item_count = dict.fromkeys(item_price_map.keys(), 0)

    for item in skus:
        try:
            item_count[item] += 1
        except KeyError:
            # Invalid SKU value
            return -1



