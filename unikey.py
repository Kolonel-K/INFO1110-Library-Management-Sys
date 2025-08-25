#validate the unikey
def validate_unikey():
    while True:
        try:
            uni_key = input("Enter your Uni-Key: ")
            # Ensures the uni_key length is 8 characters long
            if len(uni_key) != 8:
                raise ValueError
            else:
                # checks if the uni-key follows the required format of first 4 characters and last 4 characters   
                alpha_part = uni_key[:4]
                num_part = uni_key[4:]
                #validates the first 4 characters (alphanumeric)
                for char in alpha_part:
                    if not char.isalpha():
                        raise ValueError
                #validates the last 4 characters, (digits)
                for num in num_part:
                    if not num.isnumeric():
                        raise ValueError
                #break the loop while the unikey is valid
                print(f"\nUnikey Validated! Welcome, {uni_key}\n")
                break
        #continue the loop if the unikey is invalid
        except ValueError:
            print("Invalid Unikey: User not found")
    
    return uni_key
# validate_unikey()