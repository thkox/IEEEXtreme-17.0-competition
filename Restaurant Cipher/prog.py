def decipher_the_message(message):
    # Count how many g, a, e, b and c are in the message:
    a = message.count('a')
    b = message.count('b')
    c = message.count('c')
    d = message.count('d')
    e = message.count('e')
    f = message.count('f')
    g = message.count('g')
    # the letter with the maximum count is the key:
    key = max(a, b, c, d, e, f, g)
    # decipher the message using the key:
    if key == a:
        return "A"
    elif key == b:
        return "B"
    elif key == c:
        return "C"
    elif key == d:
        return "D"
    elif key == e:
        return "E"
    elif key == f:
        return "F"
    elif key == g:
        return "G"
    
if __name__=="__main__": 
    number_of_messages = int(input())
    for i in range(number_of_messages):
        message = input()
        print(decipher_the_message(message))