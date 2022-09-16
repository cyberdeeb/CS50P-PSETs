def main():
    z = fuel()
    # Output if function
    if z >= 99:
        print("F")
    elif z <= 1:
        print("E")
    else:
        print(f"{z}%")

def fuel():
    while True:
        # Pass error values to get correct input
        try:
            # Calculate percentage if smaller that 100%
            fraction = input("Fraction: ")
            x,y = fraction.split('/',3)
            calc = (int(x) / int(y)) * 100
            if calc <= 100:
                return round(calc)
        except (ValueError, ZeroDivisionError):
            pass

main()