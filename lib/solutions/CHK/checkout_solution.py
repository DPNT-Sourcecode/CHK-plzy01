from .pricing import item_price_map, specials
from .offers import OfferTypes

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
    item_count = process_type2_offers(item_count)

    # process_type3_offers()

    total_value = 0
    for item, price in item_price_map.items():
        if item not in specials[OfferTypes.TYPE_1].keys():
            total_value += item_count[item] * price
        else:
            group_offers_total, remainder_count = process_type1_offers(item, item_count)

            individual_total = remainder_count * item_price_map[item]
            total_value += individual_total + group_offers_total
    
    return total_value


def process_type1_offers(item: str, item_count: dict) -> tuple[int, int | None]:
    remainder_count = None
    total_value = 0
    for offer in specials[OfferTypes.TYPE_1][item]:
        if remainder_count is not None:
            total_remaining = remainder_count
            remainder_count =  total_remaining % offer.multiple
            group_count = (total_remaining - remainder_count) // offer.multiple
        else:
            remainder_count =  item_count.get(item, 0) % offer.multiple
            group_count = (item_count.get(item, 0) - remainder_count) // offer.multiple
    
        total_value += group_count * offer.value

    return total_value, remainder_count


def process_type2_offers(item_count: dict) -> dict:
    for item, offers in specials[OfferTypes.TYPE_2].items():
        for offer in offers:
            remainder_count = item_count.get(item, 0) % offer.multiple
            group_count = (item_count.get(item, 0) - remainder_count) // offer.multiple

            item_count[offer.item] = max(item_count[offer.item] - group_count, 0)       
    
    return item_count


def process_type3_offers(item_count: dict, item_price_map: dict) -> dict:
    total_discounted_value = 0
    for offer in specials[OfferTypes.TYPE_3]:
        eligible_item_total = 0
        for item in offer.items:
            eligible_item_total += item_count[item]
    
        total_groupings = (eligible_item_total - (eligible_item_total % offer.multiple)) // offer.multiple
        total_discounted_value += total_groupings * offer.value

        # Gives us a mapping of items sorted by value, in descending order.
        sorted_item_price_map = sorted(item_price_map.items(), key=lambda item: item[1], reverse=True)

        # Highest value items should be discounted first.
        for item in sorted_item_price_map:
            while item_count[item] > 0 and eligible_item_total > 0:
                item_count[item] -= 1
                eligible_item_total -= 1
    
    return 
    


