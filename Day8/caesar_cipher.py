from caesar import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

run = True
         

def caesar(type, message, shift_number):
    new_text = ""
    if shift_number > 26:
        shift_number = shift_number % 26
    for char in message:
        if char == " " or char in "0123456789" or char not in alphabet:
            new_text += char    
        else:
            my_index = alphabet.index(char)
            if type == "encode":
                shifted_index = my_index + shift_number
                if shifted_index > 25:
                    shifted_index -= 26
            elif type == "decode":
                shifted_index = my_index - shift_number
                if shifted_index < 0:
                    shifted_index += 26
            else:
                print(f"You did not choose right.")
                break
            new_text += alphabet[shifted_index]
    print(f"Your text is: {new_text}")

while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(type=direction, message=text, shift_number=shift)
    answer = input(f"Would like to restart? Type 'yes' or 'no' ")
    if answer == "no":
        run = False
        print(f"Goodbye")
