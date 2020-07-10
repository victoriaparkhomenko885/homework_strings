def input_number():
    number = input("Input your natural number:  ")
    try:
        number = int(number)
        if number > 0:
            return number
        else:
            return 0
    except ValueError:
        print("Natural number!")
        return 0


def check():
    check_number = input_number()
    x = 1
    while x < check_number:
        x *= 2
        if x == check_number:
            print("This number is a power of two ", check_number)
        else:
            print("This number isn't a power of two ", check_number)


check()
