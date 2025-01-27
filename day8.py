alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
              'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
              'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
             end_text += char
    print(f"The {cipher_direction}d text is {end_text}")

should_continue = True
while should_continue:    
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt\n")
    text = input("Enter your message: \n").lower()
    shift = int(input("Type the shift number: "))
    shift %= 26 # if shift number exceeds 52
    caeser(start_text= text, shift_amount= shift, cipher_direction= direction)
    result = input("Type 'yes' to continue and 'no' to end.")
    if result =='no':
         should_continue = False
    print("Goodbye")