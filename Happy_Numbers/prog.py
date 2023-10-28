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

# numpy and scipy are available for use
import numpy
import scipy

def is_Happy_num(n):
    def get_next(num):
        return sum(int(digit) ** 2 for digit in str(num))
    
    slow = n
    fast = n
    while True:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
        if slow == fast:
            break
    
    return slow == 1


a = get_number()
b = get_number()

counter = 0

for i in range(a, b+1):
    if is_Happy_num(i):
        counter += 1

print(counter)