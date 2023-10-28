v0 = int(input("Enter a: "))
v1 = int(input("Enter b: "))
v2 = int(input("Enter c: "))
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

# :l0
v11 = v11 + v1
v10 = v10 + v0
v13 = v10
v14 = v4
v15 = v4

# :l1
v16 = v13 + v13
if v16 <= v1:
    continue # :l2
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

# :l4
v17 = v17 + v13
v18 = v18 + v3
if v18 <= v6:
    continue # :l4
v18 = v3

# :l5
v17 = v17 + v9
v18 = v18 + v3
if v18 <= v12:
    continue # :l5
if v17 >= v4:
    continue # :l6

# :l6
v12 = v12 + v3
if v12 <= v2:
    continue # :l0

print(v6)