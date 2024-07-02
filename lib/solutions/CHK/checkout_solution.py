

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
    
    total_value = 0
    # specials
    specials = {
        "A": (3, 130),
        "B": (2, 45),
    }

    # Price up items with special offers
    for item, offer in specials.items():
        offer_multiple, offer_value = offer
        individual_count = item_count.get(item, 0) % offer_multiple
        group_count = (item_count.get(item, 0) - individual_count) // offer_multiple

        individual_total = individual_count * item_price_map[item]
        group_total = group_count * offer_value

        total_value += individual_total + group_total

    # Price up individual items without offers
    for item, price in item_price_map.items():
        if item not in specials.keys():
            total_value += item_count[item] * price

    return total_value

    
    

    







