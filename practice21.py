alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
              'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
              'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt and 'decode' to decrypt\n")
text = input("Enter your message: \n").lower()
shift = int(input("Type the shift number: "))

def encrypt(plain_text, shift_number):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_number
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The ecoded text is {cipher_text}")

def decrypt(cipher_text, shift_number):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_number
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")

if direction == "encode":
    encrypt(plain_text= text, shift_number= shift)
elif  direction == "decode":
    decrypt(cipher_text= text, shift_number= shift)