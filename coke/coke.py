def coke():

# Initialize amount_due
    amount_due = 50

# Loop until amount_due reaches 0
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coins = int(input("Insert Coins: "))

        # Loop to ensure only 25, 10, 5 are inputted by user
        while coins in [25, 10, 5]:

            #calculate amount_due
            amount_due -= coins
            break

# Print change
    change = abs(amount_due)
    print(f"Change Owed: {change}")


coke()