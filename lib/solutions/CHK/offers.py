
# TODO: better names
class OfferType1:
    """ Multibuy offer. e.g buy x amount of A for a discounted price"""
    multiple: int
    value: int

    def __init__(self, multiple: int = None, value: int = None) -> None:
        self.multiple = multiple
        self.value = value


class OfferType2:
    """ Buy x amount of A get B free """
    multiple: int
    item: str

    def __init__(self, multiple: int = None, item: str = None) -> None:
        self.multiple = multiple
        self.item = item