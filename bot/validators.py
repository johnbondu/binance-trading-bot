def validate_side(side):

    valid_sides = ['BUY', 'SELL']

    if side not in valid_sides:
        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type):

    valid_types = ['MARKET', 'LIMIT']

    if order_type not in valid_types:
        raise ValueError("Order type must be MARKET or LIMIT")
    
def validate_quantity(quantity):

    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than 0")