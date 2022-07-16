def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

def length(s):
    if len(s) < 2 or len(s) > 6:
        return False

# “All vanity plates must start with at least two letters.”

def letters(s):
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.

def middle(s):
    for i in range(len(s) - 1):
        if s[i].isnumeric() and s[i + 1].isalpha():
            return False

# The first number used cannot be a ‘0’.”

def check(s):
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i += 1

# “No periods, spaces, or punctuation marks are allowed.”

def punctuation(s):
    for c in s:
        if c in [".", "?", "!", " "]:
            return False

def is_valid(s):
    if length(s) != False and letters(s) != False and middle(s) != False and check(s) != False and punctuation(s) != False:
        return True
    else:
        return False


main()



