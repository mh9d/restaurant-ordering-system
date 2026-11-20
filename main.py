"""
main.py
-------
Restaurant Ordering System - entry point.
Run with:  python main.py

Shows the main menu and connects the other modules:
  menu_data.py  -> menu items and prices
  order.py      -> cart functions and bill calculation
  receipt.py    -> receipt printing and saving
  utils.py      -> input validation and formatting
"""

from menu_data import RESTAURANT_NAME, PROMO_CODES, CURRENCY
from order import (display_menu, add_item, remove_item, display_cart,
                   calculate_bill, MAX_QTY_PER_ITEM)
from receipt import build_receipt, save_receipt
from utils import get_int, get_non_empty, get_yes_no, print_header, money

ORDER_TYPES = {1: "Dine-in", 2: "Takeaway"}


def show_main_menu():
    """Print the main menu options."""
    print_header(RESTAURANT_NAME)
    print("  1. View menu")
    print("  2. Add item to order")
    print("  3. Remove item from order")
    print("  4. View current order")
    print("  5. Checkout")
    print("  6. Exit")


def handle_add(cart):
    """Ask which item and how many, then add it to the cart."""
    display_menu()
    item_id = get_non_empty("\nEnter item code (e.g. M1): ")
    qty = get_int("Quantity: ", 1, MAX_QTY_PER_ITEM)
    print("  " + add_item(cart, item_id, qty))


def handle_remove(cart):
    """Ask which item and how many, then remove it from the cart."""
    if not cart:
        print("\nYour order is empty, nothing to remove.")
        return
    display_cart(cart)
    item_id = get_non_empty("\nEnter item code to remove: ")
    qty = get_int("Quantity to remove: ", 1)
    print("  " + remove_item(cart, item_id, qty))


def ask_promo_code():
    """Ask for an optional promo code. Returns a valid code or None."""
    if not get_yes_no("Do you have a promo code?"):
        return None
    for attempt in range(3):  # give the user up to 3 tries
        code = input("Enter promo code: ").strip().upper()
        if code in PROMO_CODES:
            print(f"  Promo applied: {int(PROMO_CODES[code] * 100)}% off.")
            return code
        print("  [!] Invalid promo code.")
    print("  No promo code applied.")
    return None


def handle_checkout(cart, order_no):
    """
    Finish the order: collect customer details, show the bill,
    take payment and print/save the receipt.
    Returns True if the order was completed.
    """
    if not cart:
        print("\nYour order is empty. Please add items first.")
        return False

    display_cart(cart)
    if not get_yes_no("\nConfirm this order?"):
        print("  Checkout cancelled. You can keep editing your order.")
        return False

    customer = get_non_empty("Customer name: ")
    print("Order type: 1. Dine-in   2. Takeaway")
    order_type = ORDER_TYPES[get_int("Choose (1-2): ", 1, 2)]
    promo_code = ask_promo_code()

    bill = calculate_bill(cart, promo_code)
    print(f"\nAmount to pay: {money(bill['total'], CURRENCY)}")

    # Payment: keep asking until the amount covers the total
    while True:
        raw = input(f"Cash received ({CURRENCY}): ").strip()
        try:
            paid = float(raw)
        except ValueError:
            print("  [!] Please enter an amount, e.g. 50 or 50.00")
            continue
        if paid < bill["total"]:
            print(f"  [!] Not enough. Still need {money(bill['total'] - paid, CURRENCY)}.")
        else:
            break

    lines = build_receipt(order_no, customer, order_type, cart, bill, promo_code)
    lines.insert(-1, f"{'Cash':<37}{money(paid, CURRENCY):>13}")
    lines.insert(-1, f"{'Change':<37}{money(paid - bill['total'], CURRENCY):>13}")
    lines.insert(-1, "=" * 50)

    print()
    print("\n".join(lines))
    path = save_receipt(order_no, lines)
    if path:
        print(f"\nReceipt saved to {path}")
    return True


def main():
    """Main program loop: show the menu and run the chosen option."""
    cart = {}        # current order: item_id -> quantity
    order_no = 1001  # first order number; goes up after each checkout

    while True:
        show_main_menu()
        choice = get_int("Choose an option (1-6): ", 1, 6)

        if choice == 1:
            display_menu()
        elif choice == 2:
            handle_add(cart)
        elif choice == 3:
            handle_remove(cart)
        elif choice == 4:
            display_cart(cart)
        elif choice == 5:
            if handle_checkout(cart, order_no):
                cart = {}        # start a fresh order for the next customer
                order_no += 1
        elif choice == 6:
            if cart and not get_yes_no("You have items in your order. Exit anyway?"):
                continue
            print("\nThank you for using the Restaurant Ordering System. Goodbye!")
            break


# Only run the program when this file is executed directly
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C or end of input: exit cleanly instead of showing an error
        print("\n\nProgram closed.")
