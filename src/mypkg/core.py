"""Core pricing utilities for mypkg.

CHANGELOG (v0.2.0):
    `discount_price` used to accept two positional numbers,
    `discount_price(price, percent)`. As of v0.2.0 it accepts a single
    `Order` object instead, so callers can attach a currency and item
    count without the function signature growing indefinitely. There is
    intentionally no backward-compatible shim -- the old call style now
    raises a TypeError.
"""

from dataclasses import dataclass


@dataclass
class Order:
    """A single order to be discounted.

    Attributes:
        price: The pre-discount price, in the order's currency.
        percent: The discount percentage to apply (0-100).
        currency: ISO currency code. Defaults to "USD".
    """
    price: float
    percent: float
    currency: str = "USD"


def discount_price(order: Order) -> float:
    """Return the price after applying the order's discount percentage.

    Args:
        order: An `Order` describing the price and discount to apply.

    Returns:
        The discounted price, rounded to 2 decimal places.

    Raises:
        ValueError: If `percent` is not between 0 and 100.
    """
    if not (0 <= order.percent <= 100):
        raise ValueError(f"percent must be between 0 and 100, got {order.percent}")
    return round(order.price * (1 - order.percent / 100), 2)
