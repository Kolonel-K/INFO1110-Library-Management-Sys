# Unikey Validation Function
def validate_unikey():
    """
    Prompts the user to enter their Uni-Key and validates its format:
    - Must be 8 characters long
    - First 4 characters: alphabetic
    - Last 4 characters: numeric
    Returns the valid Uni-Key as a string.
    """
    while True:
        try:
            uni_key = input("Enter your Uni-Key: ")
            # Check length
            if len(uni_key) != 8:
                raise ValueError
            # Check first 4 are alphabetic
            if not uni_key[:4].isalpha():
                raise ValueError
            # Check last 4 are numeric
            if not uni_key[4:].isdigit():
                raise ValueError
            print(f"\nUnikey Validated! Welcome, {uni_key}\n")
            return uni_key
        except ValueError:
            print("Invalid Unikey: User not found")