def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_no_sign = d.removeprefix('$')
    return float(d_no_sign)


def percent_to_float(p):
    p_no_sign = p.removesuffix("%")
    percent = float(p_no_sign) / 100
    return percent

main()