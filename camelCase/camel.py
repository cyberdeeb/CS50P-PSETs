def camel():

    # Input from user and print
    word = input("Camel Case: ")

    # Iterate over input for uppercase letter
    for letter in word:
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else:
            print(letter, end="")

    # Print new line
    print()

camel()
