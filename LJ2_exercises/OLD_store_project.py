def main():
    
    #VARIABLES

    items_dict = { "Item 1" : {"price" : 200, "quantity" : 0},
                   "Item 2" : {"price" : 400, "quantity" : 0},
                   "Item 3" : {"price" : 600, "quantity" : 0}}
    
    total = 0

    combo_discount = 0.9

    gift_discount = 0.75

    items_list = ["Item 1", "Item 2", "Item 3"]

    user_cart = []

    store_open = True


    #FUNCTIONS

    def items_counter(user_cart, items_dict):
        for i in user_cart:
            for j in items_dict:
                if i == j:
                    items_dict[j]["quantity"] += 1


    def add_to_cart(i):
        user_cart.append(items_list[i])
        print('-'*30)
        print(items_list[i], "added to the cart.\n-------")

    def discount_checker():
        pass

    def remove_last_item():
        if len(user_cart) == 0:
            print("-------\nCart already empty!\n-------")
        else:
            user_cart.pop()

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

        items_counter(user_cart, items_dict)

        total = total_counter(items_dict)

        print("-------\n1) Item 1\n2) Item 2\n3) Item 3\nd) Delete last item\np) Purchase Items\nq) Quit")

        print("-------\nYour cart: ", user_cart)

        print("-------\nTotal = ", total)

        print("-------\nOverview = ", items_dict)
            
        user_input = input("-------\nChoose an Option and press Enter: ") # Gets the user input which is checked against the following "if" statements

        if user_input == "1":
            add_to_cart(0)

        elif user_input == "2":
            add_to_cart(1)

        elif user_input == "3":
            add_to_cart(2)
        
        elif user_input == "p": # Purchase items
            items_counter(user_cart, items_dict)
            print("The items dict is: ", items_dict)
            total = total_counter(items_dict)
            print("Total: ", total)
            discount_checker()

        elif user_input == "d": # Delete last item in the list
            remove_last_item()
            
        elif user_input == "q":
            print("-------\nClosing the store, see you next time!")
            store_open = False

        else: 
            print("-------\nInvalid input, try again!")
            
            
main()