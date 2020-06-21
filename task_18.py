def input_number():
    number = input("Input your natural number  ") 
    try:
        number = int(number)
        if(number>0):
            return number
        else:
            return 0
    except ValueError:
        print("natural number!")
        return 0

def Check():
    CheckNumber = input_number()
    i = 1
    while i < CheckNumber:
        i = i * 2
        if i == CheckNumber:
            print("This number is a power of two ",CheckNumber)
        else:
            print("This number isn't a power of two ",CheckNumber)

Check()