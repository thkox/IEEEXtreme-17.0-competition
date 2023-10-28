input = input().split()
v0 = int(input[0])
v1 = int(input[1])
v2 = int(input[2])
v3 = 1
v4 = v3 + v3
v5 = v4 + v3 
v6 = v3 
v7 = v4 
v7 = v7 - v1
v8 = v0
v9 = v0
v9 = v0 + v1
v10 = v4
v11 = v4
v12 = v3

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
            break # :l2
        v13 = v13 + v1
        v14 = v14 + v3
        v15 = v15 + v1
        # go to :l1

    # :l2
    if v13 > v4:
        continue # :l3
    v13 = v4 + v13

    # :l3
    v17 = v4
    v18 = v3

    while v18 <= v6:
        # :l4
        v17 = v17 + v13
        v18 = v18 + v3

    while v18 <= v12:
        # :l5
        v17 = v17 - v9
        v18 = v18 + v3
        if v18 <= v12:
            continue
            if v17 >= v4:
                break

    # :l6
    v12 = v12 + v3
    if v12 > v2:
        break # :l0

print(v6)