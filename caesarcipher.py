# Defining Variables 
# prompting user for the plaintext they want to encrypt
#secret_message = input("Enter your secret message: ")
# prompting user for the number of shifts they want to encrypt their message with
shift_amount =  int(input("Enter your desired shift amount: "))
# prompting user for the message the want to decrypt
#cipher_text = input("Enter your encrypted message: ")

# Defining alphabet in a dictionary
alphabet = {
    "a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4,
    "f" : 5, "g" : 6, "h" : 7, "i" : 8, "j" : 9, "k" : 10,
    "l" : 11, "m" : 12, "n" : 13, "o" : 14, "p" : 15,
    "q" : 16, "r" : 17, "s" : 18, "t" : 19, "u" : 20,
    "v" : 21, "w" : 22, "x" : 23, "y" : 24, "z" : 25
}

# Shifting method
def shifting_alphabet(shift_amount):
    # will store the new alphabet in a dictionary
    shifted_alphabet = {}
    # go through each item in alphabet
    for k, v in alphabet.items():
        # shift the original value
        shifted_value = (v + shift_amount) % 26
        # set new value to the key
        shifted_alphabet[k] = shifted_value
    return shifted_alphabet
    
print(shifting_alphabet(shift_amount))

# Encryption method
#def encryption(secret_message):
    # will store encrypted characters from secret message in a list
    #encrypted_message = []

    #for char in secret_message:
        #if char.isupper():
            #char = char.lower()