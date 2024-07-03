from enum import Enum

class OfferTypes(Enum):
    TYPE_1 = 0
    TYPE_2 = 1
    TYPE_3 = 2


# TODO: better names
class OfferType1:
    """ Multibuy offer. e.g buy x amount of A for a discounted price"""
    multiple: int
    value: int

    def __init__(self, multiple: int = None, value: int = None) -> None:
        self.multiple = multiple or 0
        self.value = value or 0


class OfferType2:
    """ Buy x amount of A get B free """
    multiple: int
    item: str | None

    def __init__(self, multiple: int = 0, item: str | None = None) -> None:
        self.multiple = multiple or 0
        self.item = item


class OfferType3:
    """ Buy any x amount of a group of items for y amount """
    multiple: int
    items: tuple[str]
    value: int

    def __init__(self, multiple: int = 0, items: tuple[str]= None, value: int = None) -> None:
        self.multiple = multiple
        self.items = items or ()
        self.value = value or 0

