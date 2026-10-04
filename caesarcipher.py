def caesar_encryption():    
    # Defining Variables 
    # prompting user for the plaintext they want to encrypt
    plain_text = input("Enter your plain message: ")
    # prompting user for the number of shifts they want to encrypt their message with
    shift_amount =  int(input("Enter your desired shift amount: "))

    # Encryption method
    def encryption(text):
        # will store encrypted characters from secret message in a list
        encrypted_list = []

        # for each character in our plain text we need to substitute them
        for char in text:

            # if the string has spaces then we have to remember those spaces
            if char == " ":
                encrypted_list.append(" ")
                continue

            # a case we need to check is if a character is uppercase, we need all letter lowercase
            if char.isupper():
                char = char.lower()

            # we use the unicode of each lowercase letter and bring it to 0-index
            # we also add our shift amount
            ord_char = ord(char) - 97
            shift_ord_char = (ord_char + shift_amount) % 26 
            shifted_char = chr(shift_ord_char + 97)
            # append it to our list
            encrypted_list.append(shifted_char)

        return "".join(encrypted_list)

    print(encryption(plain_text))

def caesar_decryption():

    encrypted_text = input("Enter you encrypted message: ")

    shift_amount = int(input("Enter the key if you know it: "))

    def decryption(text):
        decrypted_list = []

        for char in text:
            if char == " ":
                decrypted_list.append(" ")
                continue

            if char.isupper():
                char = char.lower()

            ord_char = ord(char) - 97
            
            shift_ord_char = ((ord_char + 26) - shift_amount) % 26
            shifted_char = chr(shift_ord_char + 97)

            decrypted_list.append(shifted_char)

        return "".join(decrypted_list)

    print(decryption(encrypted_text))


print("Welcome to the Caesar Cypher")
print("Choose to Encrypt or Decrypt")
print("If choosing Encryption, enter 1")
print("If choosing Decryption, enter 2")
choice = int(input("->"))
if choice == 1:
    caesar_encryption()
elif choice == 2:
    caesar_decryption()
