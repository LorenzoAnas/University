import json # To display the dictionary in a more visible way

def main():
    
    #VARIABLES

    items_dict = { "Item 1" : {"price" : 200, "quantity" : 0},
                   "Item 2" : {"price" : 400, "quantity" : 0},
                   "Item 3" : {"price" : 600, "quantity" : 0}
                   }
    
    total = 0

    combo_discount = 0.9

    gift_discount = 0.75

    store_open = True


    #FUNCTIONS

    def items_counter():
        pass


    def add_to_cart(item):
        items_dict[item]["quantity"] += 1
        last_item_added = item
        print('-'*30)
        print(items_dict[item], "added to the cart.\n-------")

    def discount_checker(i=items_dict):
        pass

        

    def clear_user_cart(i=items_dict):
        for item in items_dict:
            items_dict[item]["quantity"] = 0
        

    def total_counter(items_dict):
        total = 0
        for item in items_dict:
            price = items_dict[item]["price"]
            quantity = items_dict[item]["quantity"]
            item_total = price * quantity
            total += item_total
        return total


    #INTERFACE

    print("-------\nWelcome to the store, select one or more items to purchase!")

    while store_open: # Create a while loop which prints the welcome interface and displays the products and some options

        formatted_dict = json.dumps(items_dict, indent=4) # With this line, the dict will be displayed on multiple line for better reading.

        total = total_counter(items_dict)

        print("-------\n1) Item 1\n2) Item 2\n3) Item 3\nd) Clear cart\np) Purchase Items\nq) Quit")

        print("-------\nTotal = ", total)

        print("-------\nOverview = ", formatted_dict)
            
        user_input = input("-------\nChoose an Option and press Enter: ") # Gets the user input which is checked against the following "if" statements

        if user_input == "1":
            add_to_cart("Item 1")

        elif user_input == "2":
            add_to_cart("Item 2")

        elif user_input == "3":
            add_to_cart("Item 3")
        
        elif user_input == "p": # Purchase items, probably not necessary as a function
            pass

        elif user_input == "c": # Clear the user cart
            clear_user_cart()
            
        elif user_input == "q":
            print("-------\nClosing the store, see you next time!")
            store_open = False

        else: 
            print("-------\nInvalid input, try again!")
            
            
main()

# Check the "match" function for controlling the discount possibility