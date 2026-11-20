"""
utils.py
--------
Helper functions for safe user input (error handling / validation)
and simple screen formatting.
"""


def get_int(prompt, min_value=None, max_value=None):
    """
    Ask the user for a whole number and keep asking until it is valid.
    Optional min_value / max_value set the allowed range.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            # Not a number, e.g. "abc" or "2.5"
            print("  [!] Please enter a whole number.")
            continue

        if min_value is not None and value < min_value:
            print(f"  [!] Number must be at least {min_value}.")
        elif max_value is not None and value > max_value:
            print(f"  [!] Number must be at most {max_value}.")
        else:
            return value


def get_non_empty(prompt):
    """Ask for text and keep asking until the user types something."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("  [!] This field cannot be empty.")


def get_yes_no(prompt):
    """Ask a yes/no question. Returns True for yes, False for no."""
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("  [!] Please type y or n.")


def print_header(title):
    """Print a title surrounded by a line, to separate screens."""
    line = "=" * 50
    print(f"\n{line}\n{title.center(50)}\n{line}")


def money(amount, currency="RM"):
    """Format a number as money with 2 decimal places, e.g. RM 12.50."""
    return f"{currency} {amount:.2f}"
