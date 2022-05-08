def main():
    time = input("What time is it? ")

# Calling convert function
    new_time = convert(time)

    # if function
    if new_time >= 7 and new_time <= 8:
        print("breakfast time")
    elif new_time >= 12 and new_time <= 13:
        print("lunch time")
    elif new_time >= 18 and new_time <= 19:
        print("dinner time")

# Convert str into float
def convert(time):
    hours, minutes = time.split(":")
    min = float(minutes) / 60
    converted = float(hours) + min
    return converted

if __name__ == "__main__":
    main()
