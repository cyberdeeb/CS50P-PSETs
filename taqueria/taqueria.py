# Menu dictionary
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Order function
def order():
    total = 0
    # Loop
    while True:
        try:
            item = input("Item: ").title()
            # Check if the item is in the menu dictionary
            if item in menu:
                # Add the item price to the total
                total += menu[item]
                # Round total to two decimals
                print("Total: ${:.2f}".format(total))
        except (KeyError,EOFError):
            # Print new line and stop the loop
            print()
            break

order()