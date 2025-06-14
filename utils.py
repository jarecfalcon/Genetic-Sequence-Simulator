#===================
# File: utils.py
#===================
import os


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title):
    """Print a header with the given title."""
    clear_screen()
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)
    print("\n")
