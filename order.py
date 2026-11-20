"""
order.py
--------
Functions that work on the customer's order (the "cart").

The cart is a dictionary:  item_id -> quantity
Example: {"M1": 2, "D1": 1} means 2 x Nasi Lemak and 1 x Teh Tarik.
"""

from menu_data import (MENU, CURRENCY, SERVICE_CHARGE_RATE, SST_RATE,
                       PROMO_CODES, find_item)
from utils import money

MAX_QTY_PER_ITEM = 20  # sensible limit to catch typing mistakes


def display_menu():
    """Print every category and item on the menu."""
    for category, items in MENU.items():
        print(f"\n--- {category} ---")
        for item in items:
            print(f"  {item['id']:<4} {item['name']:<28} {money(item['price'], CURRENCY):>10}")


def add_item(cart, item_id, quantity):
    """
    Add quantity of item_id to the cart.
    Returns a message describing what happened.
    """
    item = find_item(item_id)
    if item is None:
        return f"Item code '{item_id}' does not exist."

    key = item["id"]
    new_qty = cart.get(key, 0) + quantity
    if new_qty > MAX_QTY_PER_ITEM:
        return f"Maximum {MAX_QTY_PER_ITEM} of one item per order."

    cart[key] = new_qty
    return f"Added {quantity} x {item['name']}."


def remove_item(cart, item_id, quantity):
    """
    Remove quantity of item_id from the cart.
    If the quantity reaches 0, the item is deleted from the cart.
    """
    key = item_id.strip().upper()
    if key not in cart:
        return f"Item '{item_id}' is not in your order."

    if quantity >= cart[key]:
        del cart[key]
        return f"Removed all {find_item(key)['name']} from your order."

    cart[key] -= quantity
    return f"Removed {quantity} x {find_item(key)['name']}."


def calculate_subtotal(cart):
    """Return the total price of all items before discount and charges."""
    subtotal = 0.0
    for item_id, qty in cart.items():
        subtotal += find_item(item_id)["price"] * qty
    return subtotal


def calculate_bill(cart, promo_code=None):
    """
    Work out the full bill and return it as a dictionary.
    Order of calculation:
      subtotal -> minus discount -> plus service charge -> plus SST
    """
    subtotal = calculate_subtotal(cart)

    discount_rate = PROMO_CODES.get(promo_code, 0) if promo_code else 0
    discount = subtotal * discount_rate
    after_discount = subtotal - discount

    service_charge = after_discount * SERVICE_CHARGE_RATE
    sst = (after_discount + service_charge) * SST_RATE
    total = after_discount + service_charge + sst

    # round() keeps the money values to 2 decimal places
    return {
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "service_charge": round(service_charge, 2),
        "sst": round(sst, 2),
        "total": round(total, 2),
    }


def display_cart(cart):
    """Print the items in the cart with line totals and the subtotal."""
    if not cart:
        print("\nYour order is empty.")
        return

    print(f"\n{'Code':<5}{'Item':<28}{'Qty':>4}{'Amount':>13}")
    print("-" * 50)
    for item_id, qty in cart.items():
        item = find_item(item_id)
        line_total = item["price"] * qty
        print(f"{item_id:<5}{item['name']:<28}{qty:>4}{money(line_total, CURRENCY):>13}")
    print("-" * 50)
    print(f"{'Subtotal':<37}{money(calculate_subtotal(cart), CURRENCY):>13}")
