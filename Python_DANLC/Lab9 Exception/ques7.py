# Custom Exceptions for Business Logic
#
# Create custom exception classes `OutOfStockError` and `InvalidOrderError`.
# Write a function `process_order` that takes an order (a dictionary with item names and quantities)
# and a stock (a dictionary with item names and available quantities) as arguments. Use exception handling to manage:
#
# Out of stock items (raise `OutOfStockError` with a suitable message).
#
# Invalid order quantities (e.g., negative or zero, raise `InvalidOrderError` with a suitable message).
#
# Test the function with various orders and stock scenarios.

mydict = {'bottles': 4, 'notebook': 3, 'pencil': 8, 'pens': 6, 'candles': 6}


class OutOfStock(Exception):
    def __init__(self):
        super().__init__("The product is out of stock")


class InvalidOrderError(Exception):
    def __init__(self):
        super().__init__("Not sufficient quantity")


def process_order(names, quant):
    if names not in mydict.keys():
        raise OutOfStock
    if quant > mydict[names]:
        raise InvalidOrderError
    print(f"Order Complete for {names}")

try:
    process_order('pens', 5)
except OutOfStock as so:
    print(so)
except InvalidOrderError as oe:
    print(oe)

