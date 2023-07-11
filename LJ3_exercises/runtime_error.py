user_input = input("""Type "blue" to crash the program: """)

def buggy_function(sky):
    if sky == "blue":
        print("The sky is blue")
        buggy_function(user_input)

    else:
        print("Avoided crash, goodbye!")
    
buggy_function(user_input)