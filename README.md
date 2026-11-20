# Restaurant Ordering System

A menu-driven Python console application for taking restaurant orders, built for the
Applied Python Programming assignment (Task 1).

## Features
- View the menu, grouped by category (Main Course, Side Dishes, Drinks, Desserts)
- Add and remove items from an order, with quantity limits
- View the current order with line totals and the subtotal
- Checkout with customer name, dine-in or takeaway, and an optional promo code
- Bill calculation: discount → 10% service charge → 6% SST
- Cash payment with change calculation
- Receipt printed on screen and saved to `receipts/order_<no>.txt`
- Input validation on every prompt (no crashes on wrong input)

## How to run
Requires Python 3.8 or newer. There are no extra libraries to install.

```bash
python main.py
```

Promo codes for testing: `STUDENT10` (10% off), `MMU15` (15% off).

## Project structure
| File | Purpose |
|------|---------|
| `main.py` | Entry point: main menu loop and checkout flow |
| `menu_data.py` | Menu items, prices, tax rates and promo codes |
| `order.py` | Cart functions: add, remove, display, bill calculation |
| `receipt.py` | Builds, prints and saves the receipt |
| `utils.py` | Input validation helpers and formatting |

## Requirements covered
| Requirement | Where |
|---|---|
| Variables and data types | int, float, str, bool, list and dict throughout |
| Input and output | `input()` and `print()` in `main.py` and `utils.py`; receipt file output |
| Decision making | menu choice in `main()`, validation checks, promo logic |
| Loops | main menu `while` loop, `for` loops over the menu and cart, retry loops |
| Functions (3 or more) | more than 15 functions across the modules |
| Modular programming | 5 Python files |
| Lists and dictionaries | `MENU` (dict of lists of dicts), `cart` (dict), `PROMO_CODES` (dict) |
| Error handling | `try/except ValueError` for numbers, `OSError` for file saving, Ctrl+C handling |
| Menu-driven interface | `show_main_menu()` + choice loop |
| Comments | module docstrings, function docstrings, inline comments |
