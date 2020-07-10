def input_number():
    max_number = input("Input your max natural number:  ")
    try:
        max_number = int(max_number)
        return max_number
    except ValueError:
        print("Natural number!")
        return 0


counter = 1
max_number = input_number()
if max_number > 0:
    while max_number != counter:
        print(counter)
        counter = counter + 1
else:
    print("Error")
