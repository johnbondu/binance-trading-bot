import argparse
import logging

from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import *
from bot.validators import validate_quantity

parser = argparse.ArgumentParser()

parser.add_argument('--symbol', required=True)
parser.add_argument('--side', required=True)
parser.add_argument('--type', required=True)
parser.add_argument('--quantity', required=True)
parser.add_argument('--price')

args = parser.parse_args()

try:

    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    print("\nORDER REQUEST")
    print("----------------")
    print("Symbol:", args.symbol)
    print("Side:", args.side)
    print("Type:", args.type)
    print("Quantity:", args.quantity)

    if args.type == 'MARKET':

        response = place_market_order(
            args.symbol,
            args.side,
            args.quantity
        )

    elif args.type == 'LIMIT':

        if not args.price:
            raise ValueError("LIMIT order requires --price")

        response = place_limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

    print("\nORDER SUCCESSFUL")
    print("----------------")
    print("Order ID:", response.get('orderId'))
    print("Status:", response.get('status'))
    print("Executed Qty:", response.get('executedQty'))
    print("Symbol:", response.get('symbol'))
    print("Side:", response.get('side'))
    print("Order Type:", response.get('type'))

    logging.info(f"SUCCESS RESPONSE: {response}")

except Exception as e:

    logging.error(f"ERROR: {str(e)}")

    print("\n ORDER FAILED")
    print("--------")
    print("Error:", e)