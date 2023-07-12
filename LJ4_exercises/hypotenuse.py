# Define a function that takes two arguments equal to the legs (l1,l2) of a right triangle
def hypotenuse(l1,l2):
    # Apply Pythagoras theorem to calculate the hypotenuse
    hyp = (l1**2 + l2**2)**(1/2)

    # Return the hypotenuse rounded to the first 2 decimals
    return round(hyp, 2)

# Create a test list to confront the results
test_list = [[3,4], [4,6], [5,10]]

# Create a for loop to iterate trhough the test_list and format a string to show the results
for i in range(len(test_list)):
    print(f"Given two legs of length {test_list[i]}, the hypotenuse is equal to {hypotenuse(test_list[i][0], test_list[i][1])}.")