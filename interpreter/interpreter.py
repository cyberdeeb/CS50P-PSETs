def calc():
    expression = input("Expression: ")

    #Split Expression
    x, y, z = expression.split(" ")

    #Convert x & y
    new_x = float(x)
    new_z = float(z)

    #if statement for calc
    if y == "+":
        result = new_x + new_z
        print (result)
    elif y == "-":
        result = new_x - new_z
        print (result)
    elif y == "*":
        result = new_x * new_z
        print (result)
    elif y == "/":
        result = new_x / new_z
        print (result)

calc()

