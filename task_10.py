def input_number():
    Max_number = input("Input your max natural number  ") 
    try:
        Max_number = int(Max_number)
        return Max_number
    except ValueError:
        print("natural number!")
        return 0


counter = 1
Max_number = input_number()
if( Max_number > 0):
    while(Max_number != counter):
        print(counter)
        counter=counter+1
else:
    print("Error")
