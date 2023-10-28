def encrypt_message(message, key):
    message_ecrypted = []
    for i in range(len(message)):
        # ceaser cipher
        ascii_message = [(ord(char) - key - 97) % 26 + 97 for char in message[i]]
        # convert ascii message to text
        message_ecrypted.append("".join([chr(ascii) for ascii in ascii_message]))
    return " ".join(message_ecrypted)
    
    
def decrypt_message(message, key):
    message_decrypt = []
    for i in range(len(message)):
        # ceaser cipher
        ascii_message = [(ord(char) - key + 97) % 26 + 97 for char in message[i]]
        # convert ascii message to text
        message_decrypt.append("".join([chr(ascii) for ascii in ascii_message]))
    return " ".join(message_decrypt)

if __name__=="__main__": 
    num_messages = int(input())
    for i in range(num_messages):
        key = int(input())
        message = input().split()
        if "the" in message:
            print(encrypt_message(message, key))
        else:
            print(decrypt_message(message, key))
