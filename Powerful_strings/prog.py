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

def findAllPossibleStrings(chars, prefix, m, n, possibleStrings):
     
    # Base case: n is 0,
    # return prefix
    if (n == 0) :
        possibleStrings.append(prefix)
        return
 
    # One by one add all characters 
    # from s and recursively 
    # call for n equals to n-1
    for i in range(m):
 
        # Next character of input added
        newPrefix = prefix + chars[i]
         
        # k is decreased, because 
        # we have added a new character
        findAllPossibleStrings(chars, newPrefix, m, n - 1, possibleStrings)

N = get_number()
M = get_number()
S = []

possibleStrings = []

for i in range(M):
    S.append(get_word())

chars = set()
for s in S:
    chars = chars.union(set(s))
chars = list(chars)
print(*chars)

findAllPossibleStrings(chars, "", M, N, possibleStrings)
print(*possibleStrings)

sum = 0

for string in possibleStrings:
    x = 0
    for s in S:
       # print(f'string: {string}, s: {s}, count: {string.count(s)}')
        x += string.count(s)
        #print(f'x: {x}')
    sum += 2**x
    #print(f'sum: {sum}')
        
print(sum%998244353)