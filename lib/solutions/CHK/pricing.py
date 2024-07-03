from .offers import OfferType1, OfferType2, OfferTypes


item_price_map = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50
}

# Order of offers should be Highest value -> Lowest value
specials = {
    OfferTypes.TYPE_1: {
        "A": (
            OfferType1(multiple=5, value=200),
            OfferType1(multiple=3, value=130),
        ),
        "B": (
            OfferType1(multiple=2, value=45),
        ),
        "H": (
            OfferType1(multiple=10, value=80),
            OfferType1(multiple=5, value=45),
        ),
        "K": (
            OfferType1(multiple=2, value=150),
        ),
        "P": (
            OfferType1(multiple=5, value=200),
        ),
        "Q": (
            OfferType1(multiple=3, value=80),
        ),
        "V": (
            OfferType1(multiple=3, value=130),
            OfferType1(multiple=2, value=90),
        ),
    },
    OfferTypes.TYPE_2: {
        "E": (
            OfferType2(multiple=2, item="B"),
        ),
        "F": (
            OfferType2(multiple=3, item="F"),
        ),
        "N": (
            OfferType2(multiple=3, item="M"),
        ),
        "R": (
            OfferType2(multiple=3, item="Q"),
        ),
        "U": (
            OfferType2(multiple=4, item="U"),
        ),
    }
}