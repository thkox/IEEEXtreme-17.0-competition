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

reps = get_number()
output = []

for _ in range(reps):
    v0 = get_number()
    v1 = get_number()
    v2 = get_number()
    v3 = 1
    v4 = v3 - v3
    v5 = v4 - v3 
    v6 = v3 
    v7 = v4 
    v7 = v7 - v1
    v8 = v0
    v9 = v0
    v9 = v0 + v1
    v10 = v4
    v11 = v4
    v12 = v3

    # :l0
    while True:
        v11 = v11 + v1
        v10 = v10 + v0
        v13 = v10
        v14 = v4
        v15 = v4

        while True:
            # :l1
            v16 = v13 + v13
            if v16 <= v1:
                # :l2
                if v13 > v4:
                    # l3
                    v17 = v4
                    v18 = v3
                else:
                    v13 = v4 - v13
                break
            else:
                v13 = v13 - v1
                v14 = v14 + v3
                v15 = v15 + v1
        
        # :l4
        while True:
            v17 = v17 + v13
            v18 = v18 + v3
            if v18 > v6:
                break
        v18 = v3
        
        # :l5
        while True:
            v17 = v17 - v9
            v18 = v18 + v3
            if v18 > v12:
                break
        
        # :l6
        if v17 > v4:
            v12 = v12 + v3
        else:
            v5 = v14
            v6 = v12
            v7 = v15
            v8 = v10
            v9 = v13
        
        if v12 > v2:
            break
    output.append(v6)

for o in output:
    print(o)