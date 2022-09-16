# Initialize grocery dictionary
groceries = {}

def list():
    # Loop
    while True:
        try:
            item = input().upper()
            # Check if the item is in the menu dictionary
            if item in groceries:
                # Add the item price to the total
                groceries[item] += 1
                # Round total to two decimals
            else:
                groceries[item] = 1

        except (KeyError,EOFError):
            # Print new line and stop the loop
            for item in sorted(groceries.keys()):
                print(groceries[item], item)
            break

list()