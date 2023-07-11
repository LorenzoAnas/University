# The idea is simple. The while loop iterates and the print function requires an age input from the user. 
while True:
    # The following try/except block makes sure that a valid input is recieved from the user,
    # otherwise it prints an error message and gets back to the input
    try:
        age = int(input("Insert your age: "))
        print("Somebody twice your age is", age*2)
        break  # For breaking out of the loop 
    
    except ValueError:
        print("Invalid input, please provide a real number!")


