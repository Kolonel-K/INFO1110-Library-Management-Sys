# Library Inventory Management Functions

def initialize_inv():
    """
    Initializes and returns a sample library inventory as a list of book titles.
    """
    lib_inventory = [
        "BookA", "BookB", "BookC", "BookD", "BookE",
        "Book1", "Book2", "Book3", "Book4", "Book5"
    ]
    return lib_inventory


def final_ouput(uni_key, final_inventory, books_borrowed, rejected_list):
    """
    Prints the final output, including books allocated, and calls the box function for formatted display.
    """
    print("\n\nOutput:")
    box(uni_key, final_inventory, books_borrowed, rejected_list)


def box(uni_key, final_inventory, books_borrowed, rejected_list):
    """
    Displays the borrowed books and other details in a formatted table/box.
    """
    # Box Headers
    line_break = "+" + "-"*50 + "+"
    books_borrowed_title = "BOOKS BORROWED"
    print(f"{line_break}\n|{books_borrowed_title:^50}|\n{line_break}")
    s_number = "S.NO"
    book_title = "BOOK TITLE"
    print(f"|{s_number:^8}|{book_title:^41}|\n{line_break}")

    # List borrowed books in table format
    for idx, book in enumerate(books_borrowed, 1):
        print(f"|{idx:^8}|{book:^41}|")
    print(line_break)

    print(f"| Total books borrowed: {len(books_borrowed)}")
    print(f"| Books Already Borrowed: {rejected_list}")
    print(f"| Unikey: {uni_key}")
    print(f"| Updated Inventory: {final_inventory}\n{line_break}")