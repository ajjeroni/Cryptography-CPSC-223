def caesar_encryption():    
    # Defining Variables 
    # prompting user for the plaintext they want to encrypt
    plain_text = input("Enter your secret message: ")
    # prompting user for the number of shifts they want to encrypt their message with
    shift_amount =  int(input("Enter your desired shift amount: "))

    # Encryption method
    def encryption(text):
        # will store encrypted characters from secret message in a list
        encrypted_list = []

        for char in text:

            if char.isupper():
                char = char.lower()

            ord_char = ord(char) - 97
            
            encrypted_list.append(ord_char)

        return encrypted_list

    print(encryption(plain_text))

caesar_encryption()