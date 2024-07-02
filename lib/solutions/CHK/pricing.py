from .offers import OfferType1, OfferType2


item_price_map = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}


specials = {
    "type1": {
        "A": (
            OfferType1(multiple=5, value=200),
            OfferType1(multiple=3, value=130),
        ),
        "B": (
            OfferType1(multiple=2, value=45),
        ),
        }
    "type2": {
        "E": (
            OfferType2(multiple=2, item="B"),
        ),
    }

}