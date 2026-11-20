"""
receipt.py
----------
Builds the final receipt, prints it, and saves it to a text file
inside the "receipts" folder.
"""

import os
from datetime import datetime

from menu_data import RESTAURANT_NAME, CURRENCY, SERVICE_CHARGE_RATE, SST_RATE, find_item
from utils import money

RECEIPT_FOLDER = "receipts"


def build_receipt(order_no, customer, order_type, cart, bill, promo_code=None):
    """Return the receipt as a list of text lines."""
    now = datetime.now().strftime("%d/%m/%Y %I:%M %p")
    lines = [
        "=" * 50,
        RESTAURANT_NAME.center(50),
        "OFFICIAL RECEIPT".center(50),
        "=" * 50,
        f"Order No : {order_no}",
        f"Date     : {now}",
        f"Customer : {customer}",
        f"Type     : {order_type}",
        "-" * 50,
    ]

    for item_id, qty in cart.items():
        item = find_item(item_id)
        line_total = item["price"] * qty
        lines.append(f"{qty:>2} x {item['name']:<30}{money(line_total, CURRENCY):>13}")

    lines.append("-" * 50)
    lines.append(f"{'Subtotal':<37}{money(bill['subtotal'], CURRENCY):>13}")
    if bill["discount"] > 0:
        lines.append(f"{'Discount (' + promo_code + ')':<37}{'-' + money(bill['discount'], CURRENCY):>13}")
    lines.append(f"{'Service charge ' + str(int(SERVICE_CHARGE_RATE * 100)) + '%':<37}"
                 f"{money(bill['service_charge'], CURRENCY):>13}")
    lines.append(f"{'SST ' + str(int(SST_RATE * 100)) + '%':<37}{money(bill['sst'], CURRENCY):>13}")
    lines.append("=" * 50)
    lines.append(f"{'TOTAL':<37}{money(bill['total'], CURRENCY):>13}")
    lines.append("=" * 50)
    lines.append("Thank you! Please come again.".center(50))
    return lines


def save_receipt(order_no, lines):
    """
    Save the receipt to receipts/order_<no>.txt.
    Returns the file path, or None if the file could not be written.
    """
    try:
        os.makedirs(RECEIPT_FOLDER, exist_ok=True)
        path = os.path.join(RECEIPT_FOLDER, f"order_{order_no}.txt")
        with open(path, "w", encoding="utf-8") as file:
            file.write("\n".join(lines) + "\n")
        return path
    except OSError as error:
        # e.g. no permission to write in this folder
        print(f"  [!] Could not save receipt: {error}")
        return None
