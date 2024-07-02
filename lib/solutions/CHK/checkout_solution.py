from .pricing import item_price_map, specials

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1

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

    for item, price in item_price_map.items():
        if item not in specials.keys():
             # Price up individual items without offers
            total_value += item_count[item] * price
        else:
            remainder_count = None
            for offer in specials[item]:
                # Price up items with special offers

                if remainder_count is not None:
                    total_remaining = remainder_count
                    remainder_count =  total_remaining % offer.multiple
                    group_count = (total_remaining - remainder_count) // offer.multiple

                else:
                    remainder_count =  item_count.get(item, 0) % offer.multiple
                    group_count = (item_count.get(item, 0) - remainder_count) // offer.multiple
            
                total_value += group_count * offer.value

            individual_total = remainder_count * item_price_map[item]
            total_value += individual_total
    
    return total_value