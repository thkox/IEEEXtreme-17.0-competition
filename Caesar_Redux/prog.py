def encrupt_message(message, key):

def decrypt_message(message, key):

if __name__=="__main__": 
    input = int(input())
    for i in range(input):
        key = int(input())
        message = input()
        if "the" in message:
            encrypt_message(message, key)
        else:
            decrypt_message(message, key)
