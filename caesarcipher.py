def get_valid_text(prompt):
    # keep prompting user until they enter only english letters and spaces
    while True:
        text = input(prompt)
        # we need at least one letter and every character must be an english letter or space
        if text.strip() and all("a" <= char <= "z" or "A" <= char <= "Z" or char == " " for char in text):
            return text
        print("Please enter only text (English letters and spaces, with at least one letter).")


def caesar_encryption():    
    # Defining Variables 
    # prompting user for the plaintext they want to encrypt
    plain_text = get_valid_text("Enter your plain message: ")
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

    # Defining Variables
    # prompting user for the encrypted text they want to decrypt
    encrypted_text = get_valid_text("Enter your encrypted message: ")

    # prompting user for the number of shifts used to encrypt their message
    shift_amount = int(input("Enter the key if you know it: "))

    # Decryption method
    def decryption(text):
        # will store decrypted characters from secret message in a list
        decrypted_list = []

        # for each character in our encrypted text we need to substitute them
        for char in text:
            # if the string has spaces then we have to remember those spaces
            if char == " ":
                decrypted_list.append(" ")
                continue

            # a case we need to check is if a character is uppercase, we need all letter lowercase
            if char.isupper():
                char = char.lower()

            # we use the unicode of each lowercase letter and bring it to 0-index
            ord_char = ord(char) - 97
            
            # we subtract our shift amount to shift back to the original letter
            shift_ord_char = ((ord_char + 26) - shift_amount) % 26
            shifted_char = chr(shift_ord_char + 97)

            # append it to our list
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
