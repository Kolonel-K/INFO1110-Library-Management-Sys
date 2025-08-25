# LIBRARY MANAGEMENT SYSTEM
# Main entry point for the Library Management System
import unikey
from borrow_books import borrow_books, book_validation
from lib_inventory import initialize_inv, final_ouput


def main_main():
    """
    Prints the Main Menu in a formatted box.
    """
    line_break = "+" + "-"*50 + "+"
    empty_line = f"|{'':^50}|"
    title = "LIBRARY MANAGEMENT SYSTEM"
    print(f"{line_break}\n|{title:^50}|\n{line_break}")
    print(empty_line)
    print(f"|{'Welcome to the Only Library in Existence!':^50}|")
    print(empty_line)
    print(line_break)


# Running the main loop 
if __name__ == "__main__":
    # Print the main menu
    main_main()

    # Initialise the Library Inventory
    lib_inventory = initialize_inv()
    
    # Validates the Unikey (student ID)
    user_unikey = unikey.validate_unikey() # Placeholder

    # Borrow the Books & Validate it
    borrowed_books = borrow_books(user_unikey, lib_inventory)
    validated_books, rejected_books, updated_inventory = book_validation(user_unikey, lib_inventory, borrowed_books)

    # Final Output
    final_ouput(user_unikey, updated_inventory, validated_books, rejected_books)
    