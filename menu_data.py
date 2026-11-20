"""
menu_data.py
------------
Stores the restaurant menu and the pricing settings.

Keeping the data in its own module means the menu can be changed
(new dishes, new prices) without touching the program logic.
"""

# Name of the restaurant, shown on the welcome screen and the receipt
RESTAURANT_NAME = "MMU Bites Cafe"

# Pricing settings (Malaysian restaurant style)
SERVICE_CHARGE_RATE = 0.10   # 10% service charge
SST_RATE = 0.06              # 6% Sales and Service Tax
CURRENCY = "RM"

# Promo codes: code -> discount rate (0.10 means 10% off the subtotal)
PROMO_CODES = {
    "STUDENT10": 0.10,
    "MMU15": 0.15,
}

# The menu is a dictionary of categories.
# Each category holds a list of items, and each item is a dictionary
# with an id, a name and a price (float).
MENU = {
    "Main Course": [
        {"id": "M1", "name": "Nasi Lemak Ayam Goreng", "price": 12.50},
        {"id": "M2", "name": "Mee Goreng Mamak", "price": 9.00},
        {"id": "M3", "name": "Chicken Chop", "price": 16.90},
        {"id": "M4", "name": "Spaghetti Bolognese", "price": 14.50},
    ],
    "Side Dishes": [
        {"id": "S1", "name": "Roti Canai", "price": 2.50},
        {"id": "S2", "name": "French Fries", "price": 6.00},
        {"id": "S3", "name": "Satay Ayam (6 pcs)", "price": 8.40},
    ],
    "Drinks": [
        {"id": "D1", "name": "Teh Tarik", "price": 3.50},
        {"id": "D2", "name": "Iced Milo", "price": 4.50},
        {"id": "D3", "name": "Fresh Orange Juice", "price": 6.50},
        {"id": "D4", "name": "Mineral Water", "price": 2.00},
    ],
    "Desserts": [
        {"id": "T1", "name": "Cendol", "price": 5.50},
        {"id": "T2", "name": "Chocolate Lava Cake", "price": 9.90},
    ],
}


def find_item(item_id):
    """Return the menu item that matches item_id, or None if not found."""
    item_id = item_id.strip().upper()
    for items in MENU.values():
        for item in items:
            if item["id"] == item_id:
                return item
    return None
