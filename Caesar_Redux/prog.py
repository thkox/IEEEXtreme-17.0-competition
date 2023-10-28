# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

def encrypt_message(message, shift_val):
    encrypted_message = ""
    for char in message:
        if char == " ":
            encrypted_message += " "
            continue
        ord_char = ord(char)
        if ord_char - shift_val < 97:
            dif = shift_val - (ord_char - 97) 
            new_ord_char = 122 - dif + 1
        else:
            new_ord_char = ord_char - shift_val
        encrypted_message += chr(new_ord_char)
    print(encrypted_message)

def decrypt_message(message, shift_val):
    decrypted_mmessage = ""
    for char in message:
        if char == " ":
            decrypted_mmessage += " "
            continue
        ord_char = ord(char)
        if ord_char + shift_val > 122:
            dif = shift_val - (122 - ord_char)
            new_ord_char = 97 + dif - 1
        else:
            new_ord_char = ord_char + shift_val
        decrypted_mmessage += chr(new_ord_char)
    print(decrypted_mmessage)

no_of_msgs = get_number()
shift_vals = []
messages = []

for i in range(no_of_msgs):
    shift_vals.append(get_number())
    messages.append(input())

for i in range(no_of_msgs):
    shift_val = shift_vals[i]
    message = messages[i]
    if " the " in message:
        encrypt_message(message, shift_val)
    else:
        decrypt_message(message, shift_val)
