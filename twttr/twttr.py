def omit():

    # Get text from the user
    text = input("Input: ")

    # Loop through the text for vowels
    for letter in text:
        if letter.lower() in ["a", "e", "i", "o", "u"]:

            # Removal of vowels
            print(letter.replace(letter,""), end = "")
        else:
            print(letter, end = "")
            
    # Print new line
    print()

omit()
