# mypkg

A tiny utility package for order pricing calculations.

## Installation

```bash
pip install mypkg
```

## Usage

Calculate a discounted price:

```python
from mypkg import discount_price

final_price = discount_price(100.0, 20)
print(final_price)
```

This applies a 20% discount to a $100 item.

## License

MIT
