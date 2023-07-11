def print_circum(radius, pi=3.14159):
    try:
        if radius < 0:
            print("Please insert a positive value for the radius")

        else:
            circumference = 2 * radius * pi
            print(f"A radius of length {radius} has a circumference of length: ", circumference) # The computation only takes place if the value provided is valid
            
    except TypeError:
        print("Invalid input, please provide a positive number!")


print_circum(7)
print_circum(-4)
print_circum("Cat")