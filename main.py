# LIBRARY MANAGEMENT SYSTEM
import unikey
from borrow_books import *
from lib_inventory import *


def main_main():
    # Prints the Main Menu
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
    
    # Validates the Unikey
    unikey = unikey.validate_unikey() # Placeholder

    # Borrow the Books & Validate it
    borrowed_books = borrow_books(unikey, lib_inventory)
    validated_books = book_validation(unikey, lib_inventory, borrowed_books)
    

    # Final Output
    final_ouput(unikey, validated_books[2], validated_books[0], validated_books[1])
    # print(validated_books)