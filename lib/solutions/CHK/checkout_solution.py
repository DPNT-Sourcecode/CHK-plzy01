

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1

    item_price_map = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }

    item_count = dict.fromkeys(item_price_map.keys(), 0)

    for item in skus:
        try:
            item_count[item] += 1
        except KeyError:
            # Invalid SKU value
            return -1

    return calculate_total(item_count, item_price_map)


def calculate_total(item_count: dict, item_price_map: dict) -> int:
    total_value = 0
    # Highest value offer to lowest value order
    specials = {
        "A": ((5, 200), (3, 130)),
        "B": ((2, 45)),
    }

    for item, price in item_price_map.items():
        if item not in specials.keys():
             # Price up individual items without offers
            total_value += item_count[item] * price
        else:
            remainder_count = 0
            for offer in specials[item]:
                # Price up items with special offers
                offer_multiple, offer_value = offer
                remainder_count = remainder_count or item_count.get(item, 0) % offer_multiple
                group_count = (item_count.get(item, 0) - remainder_count) // offer_multiple

            individual_total = remainder_count * item_price_map[item]
            group_total = group_count * offer_value

            total_value += individual_total + group_total
    
    return total_value

