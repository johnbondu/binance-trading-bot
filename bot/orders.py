from bot.client import client
import logging


def place_market_order(symbol, side, quantity):

    logging.info(
        f"Placing MARKET order | Symbol={symbol} Side={side} Quantity={quantity}"
    )

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type='MARKET',
        quantity=quantity
    )

    logging.info(f"MARKET ORDER RESPONSE: {order}")

    return order


def place_limit_order(symbol, side, quantity, price):

    logging.info(
        f"Placing LIMIT order | Symbol={symbol} Side={side} Quantity={quantity} Price={price}"
    )

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type='LIMIT',
        quantity=quantity,
        price=price,
        timeInForce='GTC'
    )

    logging.info(f"LIMIT ORDER RESPONSE: {order}")

    return order