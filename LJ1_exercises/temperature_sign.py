def temp_converter(T, celsius_to_fahrenheit=True):
    """T is the temperature to convert and celsius_to_fahrenheit=True is a switch that inverts the behaveiour of the function if needed"""
    if celsius_to_fahrenheit == True:
        return (T*(9/5)) + 32
    
    else:
        return (T-32)*(5/9)

while True:
    print("""Welcome to the Celsius/Fahrenheit converter. \nPress 1 if you want to convert from °C to °F \nPress 2 if you want to convert from °F to °C""")

    conversion_input = input('')

    if conversion_input != '1' and conversion_input != '2':
        print('Invalid selection, try again!')

    try:
        print('-'*30)
        temp_input = int(input("Insert the temperature of your city today: "))
        
        if conversion_input == '1':
            converted_temp = temp_converter(temp_input)
            print("In Fahrenheit is °", round(converted_temp, 2))
            break

        else:
            converted_temp = temp_converter(temp_input, celsius_to_fahrenheit=False)
            print("In Celsius is °", round(converted_temp, 2))
            break
        



    except ValueError:
        print("Invalid input, provide a number")

    

