alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n" ) 
    text = input("Type your message:\n" ).lower() 
    shift = int(input("Type the shift number:\n" )) 

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabets.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabets[new_position]
#         cipher_text += new_letter
#     print(f'The encoded text is {cipher_text}')


# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in plain_text:
#         position = alphabets.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabets[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {plain_text}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)

    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for letter in start_text:
            if letter in alphabets:
                position = alphabets.index(letter)
                new_position = position + shift_amount
                end_text += alphabets[new_position]
            else: 
                end_text += letter 
        print(f"The {cipher_direction}d text is {end_text}")
        

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if result == 'no':
        should_continue = False
        print("Good Bye!")