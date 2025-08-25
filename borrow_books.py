
def borrow_books(unikey, lib_inventory): 
    # Converts the user_input string into a list

    #inital user_input list
    borrow_books_list = [] 
    input_books = input("Enter books to borrow (comma separated): ") 
    
    #using .split to make book enteries into diff indexes(,) and .strip to remove whitespaces
    borrow_books_list = [book.strip() for book in input_books.split(",")]
    
    return(borrow_books_list)



def book_validation(uni_key,lib_inventory,borrow_books_list):
    # Validate if book is in inventory
    validated_list = []
    rejected_list = []
    for books in borrow_books_list: #reiterating the remade list
        if books in lib_inventory: #Comparing borrowed list with inventory
            validated_list.append(books)
            lib_inventory.remove(books) #Updating the inventory
        else:
            if books in lib_inventory:
                rejected_list.append(books)
            else:
                if len(books) != 0:
                    print(f"{books} not found.")

    
    return (validated_list, rejected_list, lib_inventory)
    
 

 


        

