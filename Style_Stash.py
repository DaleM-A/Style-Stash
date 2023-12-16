'''
    Style Stash
    
    An application that helps you manage your shopping trips so you can stay on top of the cost.

    Ask the user what they want to do by allowing them to add whatever item they like

    Show the customer their shopping cart before adding/removing items

    Show the user the total cost after adding/removing items

    Allow them to checkout by selecting the correct option
    
'''
# Function to display the cart each time the user makes a choice

def display_cart(cart):
    print("\n")
    print("Current items in your cart:")
    print("\n")
    for item, price in cart.items():
        print(f"{item}: £{price}")
    print("-" * 80)


print("\n")
print("Welcome to Style Stash!")
print("-"*80)

# Initialising an empty cart as a dictionary
cart = {}


# Display the user menu and cart until checkout
done = False


while (not done):
    print("\n")
    print("-"*80)
    print("Would you like to: ")
    print("\n")
    print("1. Add an item to your cart")
    print("2. Remove an item from your cart")
    print("3. View the total cost of your cart")
    print("4. Checkout")
    print("\n")
    choice = input("Enter the number of the option you would to choose:\n")

    if choice == "1": # Choice for adding an item
        item = input("What item would you like to add to your cart: ")
        while True:
            try:
                price = float(input("How much does the item cost: £"))
                break
            except ValueError:
                print("Please enter the price in numbers")
        cart[item] = price
        print("\n")
        print(f"{item} has been added to your cart.")
        display_cart(cart)

    elif choice == "2": #Choice for removing an item
        remove = input("What item would you like to remove from your cart?: ")
        if remove in cart:
            del cart[remove]

            print(f"{remove} has been removed from your cart successfully.")
        else:
            print("This item is not in your cart")
        display_cart(cart)
        

    elif choice == "3": #Choice to view the total cost of the cart
        total_cost = sum(cart.values())
        print("\n")
        print(f"The total cost of your cart is: £{total_cost}")
        display_cart(cart)

    elif choice == "4": #Choice to exit the program
        display_cart(cart)
        print("Thank you for using Style Stash!")
        break

    else:
        print("This is not a valid option. Please enter a number from 1 to 4. ")



