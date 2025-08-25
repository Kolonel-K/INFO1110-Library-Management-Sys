# 📚 Library Management System (Python CLI)
 
A simple command-line Library Management System written in Python. This project allows users to borrow books from a sample library inventory, validates user identity via Uni-Key, and displays all actions in a clean, formatted output. Designed for learning and demonstration purposes, it showcases basic Python programming, input validation, and list management.

## ✨ Features
- 🏫 **Main Menu:** Welcoming interface with a formatted menu.
- 🗝️ **Uni-Key Validation:** Ensures only valid users (8-character Uni-Key: 4 letters + 4 digits) can borrow books.
- 📚 **Book Inventory:** Predefined list of available books.
- 📝 **Borrow Books:** Users can request multiple books at once (comma separated).
- ✅ **Validation:** Checks if requested books are available and updates inventory accordingly.
- 📦 **Formatted Output:** Displays borrowed books, rejected requests, and updated inventory in a table.

## ⚙️ Installation & Setup
1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/library-management-sys.git
cd library-management-sys
```
2. Run the program:
```bash
python main.py
```
No extra dependencies required — only Python’s built-in modules.

## 🚀 Usage
- Launch the program with `python main.py`.
- Enter your Uni-Key (must be 4 letters followed by 4 digits, e.g., `abcd1234`).
- Enter the books you wish to borrow, separated by commas (e.g., `BookA, Book1, BookX`).
- The system will display which books were successfully borrowed, which were unavailable, and the updated inventory.

## 🔧 Customization
**Library Inventory:**
- The list of available books is defined in `lib_inventory.py` in the `initialize_inv()` function. Edit this list to add or remove books.

**Validation Rules:**
- Uni-Key format and book validation logic can be adjusted in `unikey.py` and `borrow_books.py` respectively.

## 📚 Learning Outcomes
- Input validation and error handling in Python.
- List and string manipulation.
- Modular code organization across multiple files.
- User interaction via command-line interface.
- Output formatting for better user experience.

## 📌 Future Improvements
- Persistent storage for inventory and user data (e.g., using files or a database).
- Return books functionality.
- Admin features for adding/removing books.
- Enhanced user authentication.
- Unit tests for core functions.

## 🧑‍💻 Author
Developed by _Kanav Veer Singh_ – A software engineering student working on Python, data storage, and CLI development.   
_(Week 4 Workshop Project - INFO1110 at The University of Sydney)_
