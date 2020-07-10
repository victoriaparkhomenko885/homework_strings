def input_number():
    number = input("Input your str:  ") 
    try:
        number = int(number)
        if number > 0:
            print("This str is natural number!")
        else:
            return 0
    except ValueError:
        print("This str isn't natural number!")
        

input_number()