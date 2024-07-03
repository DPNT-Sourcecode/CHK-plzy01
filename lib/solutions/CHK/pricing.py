from .offers import OfferType1, OfferType2, OfferTypes


item_price_map = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
}


specials = {
    OfferTypes.TYPE_1: {
        "A": (
            OfferType1(multiple=5, value=200),
            OfferType1(multiple=3, value=130),
        ),
        "B": (
            OfferType1(multiple=2, value=45),
        ),
    },
    OfferTypes.TYPE_2: {
        "E": (
            OfferType2(multiple=2, item="B"),
        ),
        "F": (
            OfferType2(multiple=3, item="F"),
        ),
    }
}
