# calculate the height of the person
def calculate_height_of_person(a, previous_height, c, q):
    return (a * previous_height + c) % q

# create a dictionary that stores the heights of the people
heights = {}

# compare heights of the people
def noticable_people(heights):
    noticable_people_number = 0
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            # extract the values between heights[i] and heights[j]
            values = list(heights.values())[i:j]
            # check if there are any values that are greater than or equal to heights[i]
            if heights[i] >= max(values):
                noticable_people_number += 1
    return noticable_people_number

# main function
if __name__=="__main__": 
    # store the five values from the terminal
    input = [int(x) for x in input().split()]

    n = input[0]
    first_person = input[1]
    a = input[2]
    c = input[3]
    q = input[4]

    for i in range(n):
        if i == 0:
            heights[i] = first_person
        else:
            heights[i] = calculate_height_of_person(a, heights[i-1], c, q)
    
    final_value = noticable_people(heights)
    print(final_value)