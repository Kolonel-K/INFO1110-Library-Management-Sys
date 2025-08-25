# Book Borrowing and Validation Functions

def borrow_books(unikey, lib_inventory):
    """
    Prompts the user to enter books to borrow (comma separated),
    returns a list of requested book titles (stripped of whitespace).
    """
    input_books = input("Enter books to borrow (comma separated): ")
    # Split input by comma and strip whitespace from each book title
    borrow_books_list = [book.strip() for book in input_books.split(",") if book.strip()]
    return borrow_books_list


def book_validation(uni_key, lib_inventory, borrow_books_list):
    """
    Validates the requested books against the inventory.
    Returns a tuple: (validated_list, rejected_list, updated_inventory)
    - validated_list: books successfully borrowed
    - rejected_list: books not available or already borrowed
    - updated_inventory: inventory after borrowing
    """
    validated_list = []
    rejected_list = []
    for book in borrow_books_list:
        if book in lib_inventory:
            validated_list.append(book)
            lib_inventory.remove(book)  # Update inventory
        else:
            if book:  # Only print message for non-empty book names
                print(f"{book} not found or already borrowed.")
            if book in lib_inventory:
                rejected_list.append(book)
    return validated_list, rejected_list, lib_inventory
