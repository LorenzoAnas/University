# I didn't want the program to be static and I've found online a library called geocoder which retrieves information based on the IP of the user.
# It can be easily installed with "pip install geocoder" from the command line.

import geocoder

def get_location():
    g = geocoder.ipinfo('me')  # Retrieve location based on IP address
    return g.city, g.country

city, country = get_location() # The 2 values returned from the get_location() function are associated with city and country

while True:
    print("""0)Asia \n1) Africa \n2) Oceania \n3) North America \n4) South America \n5) Europe""")

    continent_list = ['Asia', 'Africa', 'Oceania', 'North America', 'South America', 'Europe']
    
    user_input = input("Type the number associated with your favourite continent: ")

    if user_input == '0':
        continent = continent_list[0]
    
    elif user_input == '1':
        continent = continent_list[1]

    elif user_input == '2':
        continent = continent_list[2]

    elif user_input == '3':
        continent = continent_list[3]
    
    elif user_input == '4':
        continent = continent_list[4]    
    
    elif user_input == '5':
        continent = continent_list[5]
    
    else:
        print("Invalid selection, here's where you are anyway.")

    print('-'*30) # I love multiplying strings, it feels so wrong!
    print("Your City:", city)
    print("Your Country:", country)
    print("Your favourite continent:", continent)
    break


