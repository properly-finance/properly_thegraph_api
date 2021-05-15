from typing import Optional


def calc_price(price: int, estate: Optional[dict]) -> int:
    if not estate:
        return price
    size = estate.get('size')
    if not size:
        return price
    return price // int(size)
