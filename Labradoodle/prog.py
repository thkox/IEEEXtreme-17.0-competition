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

n = get_number()
m = get_number()

dictionary = []

for i in range(n):
    dictionary.append(get_word())

output = []

for i in range(m):
    word = get_word()
    if len(word) <= 4:
        output.append('none')
        continue
    
    prefix = word[0:3]
    suffix = word[-3:]
    counter = 0
    first_word = None
    second_word = None
    is_ambiguous = False
    
    for word in dictionary:
        if counter >= 2:
            is_ambiguous = True
            break
        if word.startswith(prefix) and word.endswith(suffix):
            counter += 1
            first_word = word
            second_word = word
        elif word.startswith(prefix):
            first_word = word
            if second_word is not None:
                counter += 1
        elif word.endswith(suffix):
            second_word = word
            if first_word is not None:
                counter += 1
    if is_ambiguous:
        output.append('ambiguous')
    elif first_word is not None and second_word is not None:
        output.append(first_word + ' ' + second_word)
    else:
        output.append('none')

for line in output:
    print(line)