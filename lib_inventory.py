
def initialize_inv():
    # Initializes a Sample Library Inventory
    lib_inventory=["BookA",
                    "BookB",
                    "BookC",
                    "BookD",
                    "BookE",
                    "Book1",
                    "Book2", 
                    "Book3", 
                    "Book4", 
                    "Book5"]
    return lib_inventory


def final_ouput(uni_key, final_inventory, books_borrowed, rejected_list):
    # Links The Final Output Function To The Inventory List For Output
    print("\n\nOutput:")
    print(f"Books Allocated To {uni_key}: {books_borrowed}")
    box(uni_key, final_inventory, books_borrowed, rejected_list)
    
 


def box(uni_key, final_inventory, books_borrowed, rejected_list):
    # Represents The Available Books In A Formatted Box

    # Box Headers
    line_break = "+" + "-"*50 + "+"
    books_borrowed_title= "BOOKS BORROWED"
    print(f"{line_break}\n|{books_borrowed_title:^50}|\n{line_break}")
    s_number= "S.NO"
    book_title = "BOOK TITLE"
    print(f"|{s_number:^8}|{book_title:^41}|\n{line_break}")
    
    # Loop to represent the list of borrowed books in the table format
    for s_number, books in enumerate(books_borrowed):
        print(f"|{s_number+1:^8}|{books:^41}|")
    print(line_break)
    
    print(f"| Total books borrowed: {len(books_borrowed)}")
    print(f"| Books Already Borrowed: {rejected_list}")
    print(f"| Unikey: {uni_key}")
    print(f"| Updated Inventory: {final_inventory}\n{line_break}")