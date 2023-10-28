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
            values = list(heights.values())[i+1:j]
            # check if there are any values that are greater than or equal to heights[i]
            if j - i == 1:
                noticable_people_number += 1
            elif heights[i] > max(values):
                noticable_people_number += 1
            else:
                break
    return noticable_people_number

# main function
if __name__=="__main__": 
    # store the five values from the terminal
    input = [int(x) for x in input().split()]

    for i in range(input[0]):
        if i == 0:
            heights[i] = input[1]
        else:
            heights[i] = calculate_height_of_person(input[2], heights[i-1], input[3], input[4])
    print(noticable_people(heights))