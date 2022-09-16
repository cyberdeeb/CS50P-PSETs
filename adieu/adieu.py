import inflect

names = []
p = inflect.engine()


def adieu():
    # Loop through user's name inputs till exception
    while True:
        try:
            people = input('Name: ')
            # Add names to initialized list
            names.append(people)
        except EOFError:
            # Add names in set format to statement
            print(f'Adieu, adieu, to {p.join(names)}')
            break

adieu()